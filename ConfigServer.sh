#!/usr/bin/env bash

# required package:
#   nginx, uwsgi, python

SELF_PATH=`cd $(dirname $0); pwd -P;`
read -e -p "Enter IP address of your config server？/ 请输入您服务器的 IP 地址:" \
    -i "39.105.214.245" SERVER_IP
read -e -p "Enter the deploy port of your config? / 请输出您需要部署的服务器 IP 地址："\
    -i "8083" SERVER_PORT
read -e -p "Enter domain name of your config server / 请输入指向您服务器的域名:" \
    -i "www.nkchatbot.com" DOMAIN_NAME
read -e -p "What is the name of your project / 您希望您项目的名称叫什么(please do not leave blank):" \
    -i "ServerAPI" PROJECT_NAME
read -e -p "What is your settings directory name or django project name / Django 设置文件所在的文件夹:" \
    -i "ServerAPI" DJANGO_PROJECT_NAME
read -e -p "What is your python virtualenv directory / 您 python 的虚拟环境在哪个地址:" \
    -i "/var/www/.virtualenvs/" WORKON_HOME
echo "---------------------------------------------------------------------------------"
read -e -p "Getting a new virtualenv / 是否需要新建一个 python 虚拟环境?[Y/others]" \
    -i "N" VIRTUALENV_CHOICE
read -e -p "Config your ip and domain name into django-settings / 是否将 IP 和域名写入 Django 的设置中?[Y/others]" \
    -i "Y" DJANGO_SETTING_CHOICE
read -e -p "Config your nginx and reload / 是否重新将配置写入 nginx 配置文件并重启 nginx?[Y/others]" \
    -i "Y" NGINX_SETTING_CHOICE
read -e -p "Config a new uwsgi inite file / 是否需要新建一个 uwsgi 的初始化 ini 文件?[Y/others]" \
    -i "Y" UWSGI_SETTING_CHOICE
read -e -p "Need shell scripts running and stopping uwsgi / 是否需要新建启动和停止 uwsgi 的脚本?[Y/others]" \
    -i "Y" UWSGI_SCRIPT_CHOICE

sudo /usr/bin/python3.6 -m pip install virtualenv virtualenvwrapper
export PYTHON=python3.6
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.6
export WORKON_HOME=${WORKON_HOME}
source `which virtualenvwrapper.sh`
case ${VIRTUALENV_CHOICE} in
    y|Y)
    mkvirtualenv ${PROJECT_NAME}
    ;;
    *) workon ${PROJECT_NAME} ;;
esac
pip install -r ./requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

cat << _EOF_ > tmp
upstream django-${PROJECT_NAME} {
    server unix://${SELF_PATH}/${PROJECT_NAME,,}.sock; # for a file socket
}
server {
    listen ${SERVER_PORT};
    server_name ${SERVER_IP} ${DOMAIN_NAME};
    charset     utf-8;
    client_max_body_size 75M;

    root ${SELF_PATH};
    index index.html index.htm index.nginx-debian.html;

    location /media {
        alias ${SELF_PATH}/media;
    }
    location /static {
        alias ${SELF_PATH}/static;
    }
    location / {
        uwsgi_pass  django-${PROJECT_NAME};
        include ${SELF_PATH}/uwsgi_params;
    }

    error_log /var/log/nginx/error.log;
    access_log /var/log/nginx/access.log;
}
_EOF_

case ${NGINX_SETTING_CHOICE} in
    y|Y)
    sudo mv tmp /etc/nginx/sites-available/${PROJECT_NAME}.conf
    sudo ln -sf /etc/nginx/sites-available/${PROJECT_NAME}.conf /etc/nginx/sites-enabled/
    sudo systemctl restart nginx
        ;;
    *) echo "nginx not config." ;;
esac

case ${DJANGO_SETTING_CHOICE} in
    y|Y)
    sed "s@ALLOWED_HOSTS = .*@ALLOWED_HOSTS = ['${DOMAIN_NAME}', '${SERVER_IP}']@g" \
        ./${DJANGO_PROJECT_NAME}/settings.py > tmp
    mv tmp ./${DJANGO_PROJECT_NAME}/settings.py
        ;;
    *) echo "Leave ALLOWED_HOSTS." ;;
esac

cat << _EOF_ > tmp
# uwsig_${PROJECT_NAME,,}.ini file
[uwsgi]
chdir           = %d
module          = ${DJANGO_PROJECT_NAME}.wsgi
virtualenv      = ${WORKON_HOME}/${PROJECT_NAME}

# process-related settings
master          = true
processes       = 10
socket          = %d${PROJECT_NAME,,}.sock
chmod-socket    = 665
# clear environment on exit
vacuum          = true
uid             = www-data
gid             = www-data
pidfile         = %dprocess_${PROJECT_NAME,,}.pid

plugins-dir     = /usr/lib/uwsgi/plugins/
plugins         = python36
_EOF_

case ${UWSGI_SETTING_CHOICE} in
    y|Y)
    mv tmp ./uwsgi_${PROJECT_NAME,,}.ini
    ;;
    *) echo "You haven't create uwsgi ini file.";;
esac

cat << _EOF_ > tmp
#!/usr/bin/env bash

cd \`dirname \$0\`

export WORKON_HOME=${WORKON_HOME}
source `which virtualenvwrapper.sh`
workon ${PROJECT_NAME}

cat <(echo "yes") | python ./manage.py collectstatic
uwsgi --ini ./uwsgi_${PROJECT_NAME,,}.ini \
    2> ./log/\`date +"%Y_%m_%d_%H:%M:%S"\`.err.log 1> ./log/\`date +"%Y_%m_%d_%H:%M:%S"\`.info.log &

sudo chown www-data:www-data ${PROJECT_NAME,,}.sock
_EOF_

case ${UWSGI_SCRIPT_CHOICE} in
    y|Y)
    mv tmp ./run_uwsgi_${PROJECT_NAME,,}.sh
    chmod +x ./run_uwsgi_${PROJECT_NAME,,}.sh
    ;;
    *) echo "You don't create run uwsgi script." ;;
esac

cat << _EOF_ > tmp
#!/usr/bin/env bash

cd \`dirname \$0\`

if [[ -f ./process_${PROJECT_NAME,,}.pid ]]; then
    uwsgi --stop ./process_${PROJECT_NAME,,}.pid
else
    read -e -p "Pid file not found. Force kill all uwsgi process?[Y/others]" -i "Y" CHOICE
    case \${CHOICE} in
        y|Y) sudo pkill -f uwsgi -9 ;;
        *) echo "You don't kill any process." ;;
    esac
fi
_EOF_

case ${UWSGI_SCRIPT_CHOICE} in
    y|Y)
    mv tmp ./stop_uwsgi_${PROJECT_NAME,,}.sh
    chmod +x ./stop_uwsgi_${PROJECT_NAME,,}.sh
    ;;
    *) echo "You don't create stop script." && rm tmp;;
esac
# Generated by Django 2.1.7 on 2019-04-02 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='必填项。老师的姓名，最多 32 个字符', max_length=32, verbose_name='姓名')),
                ('sex', models.CharField(choices=[('男', '男性'), ('女', '女性')], help_text='必填项，性别。', max_length=2, verbose_name='性别')),
                ('email', models.CharField(blank=True, help_text='老师的电子邮箱，最多 64 个字符', max_length=64, null=True, verbose_name='电子邮件')),
                ('tele', models.CharField(blank=True, help_text='老师的电话号码，最多 64 个字符。', max_length=64, null=True, verbose_name='电话号码')),
                ('admin', models.CharField(blank=True, help_text='老师在学院里担任的官职，最多 64 个字符', max_length=64, null=True, verbose_name='官职')),
                ('major', models.CharField(blank=True, help_text='老师的毕业方向，最多 64 个字符', max_length=64, null=True, verbose_name='毕业方向')),
                ('field', models.CharField(blank=True, help_text='老师的研究方向，最多 64 个字符', max_length=64, null=True, verbose_name='研究领域')),
                ('degree', models.CharField(blank=True, help_text='老师的学位，最多 64 个字符', max_length=64, null=True, verbose_name='学位')),
                ('title', models.CharField(blank=True, help_text='老师的职称，最多 64 个字符', max_length=64, null=True, verbose_name='职称')),
                ('depart', models.CharField(blank=True, help_text='老师的所属院系，最多 64 个字符', max_length=64, null=True, verbose_name='院系')),
                ('URL', models.CharField(blank=True, help_text='介绍老师的网页链接，最多 128 个字符', max_length=128, null=True, verbose_name='链接')),
            ],
            options={
                'verbose_name': '教师对象',
                'verbose_name_plural': '教师表格',
            },
        ),
    ]

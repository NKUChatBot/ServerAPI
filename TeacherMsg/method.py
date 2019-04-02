import jieba

from .models import Teacher
from .find_keyword.keyword import keywords
from .find_college.findKey import find_college

def response(question):
    ## 从问题中提取关键字
    Qname=keywords(question)# find teacher_name
    Qcollege=find_college(question) ## find college_name
    
    names = {dic["pk"]:dic["name"] for dic in Teacher.objects.all().values("name", "pk")}
    college={dic["pk"]:dic["college"] for dic in Teacher.objects.all().values("college", "pk")}
    #words = jieba.cut(question)
    if len(Qcollege)==0:
        qlist=Teacher.objects.filter(name=Qname)# list
        if len(qlist)==1:
            teacher = qlist.values().first()
            return ';'.join([f'{k}是{v}' for k, v in teacher.items()])
        else:
            return '学院？'
    else:
        qlist=Teacher.objects.filter(name=Qname,college=Qcollege)
        if len(qlist):
            teacher = qlist.values().first()
            return ';'.join([f'{k}是{v}' for k, v in teacher.items()])
        
#    for pk,name in names.items():
#        
#        if Qname in name:
#            teacher = Teacher.objects.filter(pk=pk).values().first()
#            return ';'.join([f'{k}是{v}' for k, v in teacher.items()])
#            
#    for word in words:
#        for pk, name in names.items():
#            if word in name:
#                teacher = Teacher.objects.filter(pk=pk).values().first()
#                return ';'.join([f'{k}是{v}' for k, v in teacher.items()])
    return None


    

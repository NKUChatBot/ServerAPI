import jieba

from .models import Teacher


def response(question):
    names = {dic["pk"]:dic["name"] for dic in Teacher.objects.all().values("name", "pk")}
    words = jieba.cut(question)
    for word in words:
        for pk, name in names.items():
            if word in name:
                teacher = Teacher.objects.filter(pk=pk).values().first()
                return ';'.join([f'{k}是{v}' for k, v in teacher.items()])
    return None

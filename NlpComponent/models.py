from django.db import models
import json


# Create your models here.

class WordVector(models.Model):
    word = models.CharField(
        max_length=32,
        primary_key=True,
        help_text=u"主键属性，最长 32 个字节",
    )
    vector = models.CharField(
        max_length=2500,
        help_text=u"向量通过其 200 维的列表 json.dumps 为字符串后替换空字符存储，<br />"
                  u"计算得到这个字符串最长 2401，数据库中以最多 2500 字节存储"
    )

    def get_vector(self):
        return json.loads(self.vector)

    def set_vector(self, vec):
        assert len(vec) == 200
        for v in vec:
            assert isinstance(v, str)
            assert len(v) < 10
        self.vector = json.dumps(vec).replace(' ', '')
        self.save()

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = "词向量"
        verbose_name_plural = "词向量数据库"


class WordVectorCache(models.Model):
    """
    暂时存储查询出来的 WordVector，提升查询效率
    这是一个冗余项，需要注意 WordVector 项目改变时，容易导致不一致
    """
    word = models.CharField(
        max_length=32,
        primary_key=True,
    )
    vector = models.CharField(
        max_length=2500
    )
    call_times = models.IntegerField(
        editable=False,
        default=1,
        help_text=u"用于记录该项被调用次数的属性值",
    )

    def increase_call_times(self):
        self.call_times += 1
        self.save()

    def get_vector(self):
        return json.loads(self.vector)

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = "词向量缓存"
        verbose_name_plural = "词向量高速缓存数据库"

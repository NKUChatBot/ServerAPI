from django.db import models
import json

# Create your models here.

class WordVector(models.Model):
    word = models.CharField(
        max_length=4,
        primary_key=True,
        help_text=u"主键属性",
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
        self.vector = json.dumps(vec).replace(' ','')
        self.save()

    def __str__(self):
        return self.word

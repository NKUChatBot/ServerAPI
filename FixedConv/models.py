from django.db import models

# Create your models here.
class Aiml(models.Model):
    pattern = models.CharField(
        max_length=128,
        help_text=u"唯一标识，以字符串形式存储在数据库中的 pattern，最长 128 个字节",
    )
    template = models.CharField(
        max_length=256,
        help_text=u"以字符串形式存储在数据库中的 template，最长 256 个字节",
    )
    that = models.CharField(
        max_length=128,
        help_text=u"以字符串形式存储在数据库中的 taht，最长 128 个字节",
    )

    def __str__(self):
        return self.pattern

    class Meta:
        verbose_name = u"模式对象"
        verbose_name_plural = u"模式表格"
        unique_together = ("pattern", "that")

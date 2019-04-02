from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(
        verbose_name=u"姓名",
        max_length=32,
        help_text=u"必填项。老师的姓名，最多 32 个字符"
    )
    sex = models.CharField(
        verbose_name=u"性别",
        max_length=2,
        choices=(("男", "男性"), ("女", "女性")),
        help_text=u"必填项，性别。"
    )
    email = models.CharField(
        verbose_name=u"电子邮件",
        max_length=64,
        null=True, blank=True,
        help_text=u"老师的电子邮箱，最多 64 个字符",
    )
    tele = models.CharField(
        verbose_name=u"电话号码",
        max_length=64,
        null=True, blank=True,
        help_text=u"老师的电话号码，最多 64 个字符。",
    )
    admin = models.CharField(
        verbose_name=u"官职",
        max_length=64,
        null=True, blank=True,
        help_text=u"老师在学院里担任的官职，最多 64 个字符",
    )
    major = models.CharField(
        verbose_name=u"毕业方向",
        max_length=64,
        null=True, blank=True,
        help_text=u"老师的毕业方向，最多 64 个字符"
    )
    field =models.CharField(
        verbose_name=u"研究领域",
        max_length=128,
        null=True, blank=True,
        help_text=u"老师的研究方向，最多 128 个字符"
    )
    degree = models.CharField(
        verbose_name=u"学位",
        max_length=64,
        null=True, blank=True,
        help_text=u"老师的学位，最多 64 个字符"
    )
    title = models.CharField(
        verbose_name=u"职称",
        max_length=64,
        null=True, blank=True,
        help_text=u"老师的职称，最多 64 个字符"
    )
    depart = models.CharField(
        verbose_name=u"研究系属",
        max_length=64,
        null=True, blank=True,
        help_text=u"老师的所属院系，最多 64 个字符",
    )
    URL = models.CharField(
        verbose_name=u"链接",
        max_length=128,
        null=True, blank=True,
        help_text=u"介绍老师的网页链接，最多 128 个字符",
    )
    college = models.CharField(
            verbose_name=u"学院",
            max_length=128,
            null=True,blank=True,
            help_text=u""
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = u"教师表格"
        verbose_name = u"教师对象"

from django.db import models
from tools import models_method


# Create your models here.
class EWSMainTable(models.Model):
    SN = models.CharField("服务码", max_length=10)
    modelName = models.CharField("型号", max_length=30, null=True)
    MAC = models.CharField("MAC", max_length=20)
    area = models.CharField("区域", max_length=10, null=True)
    line = models.CharField("线号", max_length=10, null=True)
    row = models.CharField("杠号", max_length=10, null=True)
    number = models.CharField("编号", max_length=10, null=True)
    created_time = models.DateTimeField("入站时间", auto_now_add=True)
    expire_time = models.DateTimeField("到期时间", default=models_method.count_expire_time())

    class Meta:
        db_table = "EWS"
        verbose_name_plural = "EWS主表"


class EWSModelInfo(models.Model):
    modelName = models.CharField("型号", max_length=30, null=True)
    duration = models.TimeField("测试时长")

    class Meta:
        db_table = "ModelInfo"
        verbose_name_plural = "机型配置信息"

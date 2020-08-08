from django.db import models


# Create your models here.
class EWSMainTable(models):
    SN = models.CharField("服务码", max_length=10)
    modelName = models.CharField("服务码", max_length=30)
    MAC = models.CharField("MAC", max_length=20)
    line = models.CharField("区域", max_length=10)
    line = models.CharField("线号", max_length=10)
    row = models.CharField("杠号", max_length=10)
    number = models.CharField("编号", max_length=10)
    created_time = models.DateTimeField("入站时间", auto_now_add=True)

    class Meta:
        db_table = "EWS"
        verbose_name_plural = "EWS主表"

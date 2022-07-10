from django.db import models
from uuid import uuid4


class BaseModel(models.Model):
    """为模型类补充字段"""
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    class Meta:
        abstract = True


def get_main_filename(path_name):
    # 查找最右边的点号位置
    dot_position = path_name.rfind('.')
    # 没有找到点号，说明只有文件名
    if dot_position == -1:
        return path_name
    # 查找最右边的/位置
    slash_posistion = path_name.rfind('/')
    # 切片
    return path_name[slash_posistion + 1:dot_position]


def get_goods_image_upload_filename(instance, filenam):
    return "goods/" + uuid4().hex + ".jpg"

from django.contrib import admin

from xiaoyu_mall.utils.models import get_main_filename
from .models import SKU, SPU


@admin.register(SKU)
class GoodsAdmin(admin.ModelAdmin):
    # 显示列表
    list_display = ['id', 'name', 'create_time', 'update_time', 'price',
                    'cost_price', 'market_price', 'stock', 'sales', 'comments']

    def save_model(self, request, obj, form, change):
        """新增或更新表中的数据时调用"""
        super().save_model(request, obj, form, change)
        # 让default_image只保存主文件名
        main_filename = get_main_filename(str(obj.default_image))
        obj.default_image = main_filename
        obj.save()


@admin.register(SPU)
class SpuAdmin(admin.ModelAdmin):
    # 显示列表
    list_display = ['name', 'brand', 'category1', 'category2', 'category3', 'sales', 'comments']

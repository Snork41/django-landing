from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.utils.safestring import mark_safe
from easy_thumbnails.files import get_thumbnailer

from .models import Slider


@admin.register(Slider)
class SliderAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = (
        'name',
        'image_slider',
        'my_order'
    )

    @admin.display(description='Превью')
    def image_slider(self, obj):
        thumbnailer = get_thumbnailer(obj.image).get_thumbnail({'size': (100, 100), 'crop': 'smart'}).url
        return mark_safe(f'<img src="{thumbnailer}">')

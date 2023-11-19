from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from django.utils.safestring import mark_safe

from .models import Slider


@admin.register(Slider)
class SliderAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = (
        'name',
        'image_slider',
        'my_order'
    )

    def image_slider(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')

    image_slider.short_description = 'Превью'

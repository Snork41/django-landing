from django.db import models
from filer.fields.image import FilerImageField


class Slider(models.Model):
    name = models.CharField(
        verbose_name='Имя изображения',
        max_length=255
    )
    image = FilerImageField(
        null=True,
        blank=True,
        related_name="image_slider",
        on_delete=models.CASCADE
    )
    my_order = models.PositiveIntegerField(
        verbose_name='drag & drop',
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['my_order']
        verbose_name = 'Изображение в слайдере'
        verbose_name_plural = 'Изображения в слайдере'
    
    def __str__(self):
        return f'Изображение для слайдера {self.name}'

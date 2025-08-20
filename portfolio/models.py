from django.db import models
from django.utils.safestring import mark_safe


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='projects/', blank=True, null=True, verbose_name="Основное изображение")  # Оставляем, но делаем необязательным
    link = models.URLField(blank=True, verbose_name="Ссылка на проект")  # Для GitHub или других ссылок
    is_github = models.BooleanField(default=False, verbose_name="GitHub проект")  # Добавлено: флаг для GitHub
    other_link = models.URLField(blank=True, null=True, verbose_name="Другая ссылка")  # Добавлено: для Tilda/Salebot
    featured = models.BooleanField(default=False, verbose_name="Избранный")  # Добавлено: для главной страницы
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")  # Добавлено: для сортировки

    class Meta:
        ordering = ['order']
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.title


class PortfolioConfig(models.Model):
    BLOCK_CHOICES = [
        ('user_info', 'User Information'),
        ('social_links', 'Social Links'),
        ('content', 'Content'),
        ('images', 'Images'),
        ('about_me', 'About me'),
    ]

    block = models.CharField(max_length=50, choices=BLOCK_CHOICES, help_text="Configuration block (e.g., USER_INFO)")
    key = models.CharField(max_length=100, help_text="Configuration key (e.g., PORTFOLIO_NAME)")
    value = models.TextField(help_text="Configuration value")

    class Meta:
        unique_together = ('block', 'key')
        verbose_name = 'Portfolio Configuration'
        verbose_name_plural = 'Portfolio Configurations'

    def __str__(self):
        return f"{self.block}: {self.key} = {self.value}"


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images', verbose_name="Проект")
    image = models.ImageField(upload_to='projects/images/', verbose_name="Изображение")
    caption = models.CharField(max_length=200, blank=True, verbose_name="Подпись")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        ordering = ['order']
        verbose_name = "Изображение проекта"
        verbose_name_plural = "Изображения проектов"

    def __str__(self):
        return f"{self.project.title} - Изображение {self.order}"

    def image_tag(self):  # Для предпросмотра в админке
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="150" />')
        return ""

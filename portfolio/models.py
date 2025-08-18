from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True)

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
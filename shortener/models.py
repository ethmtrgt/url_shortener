from django.db import models

class ShortUrl(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    alias = models.CharField(max_length=32, unique=True, null=False, verbose_name='Alias')
    long_url = models.URLField(verbose_name='Long URL')
    visits = models.PositiveIntegerField(default=0, verbose_name='Visits')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')

    def __str__(self):
        return f'ID: {self.id}, Alias: {self.alias}, {self.visits} visits.'

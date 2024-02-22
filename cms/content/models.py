from django.db import models

class ContentItem(models.Model):
    title = models.CharField(max_length=30, verbose_name='Title')
    body = models.TextField(max_length=300, verbose_name='Body')
    summary = models.CharField(max_length=60, verbose_name='Summary')
    document=models.FileField(upload_to="pdfs",verbose_name='Document')
    categories = models.ManyToManyField('Category', related_name='content_items', verbose_name='Categories')

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Name')

    def __str__(self):
        return self.name

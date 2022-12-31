from django.db import models
from datetime import datetime

class Category(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return f"{self.name}"

class Article(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    title = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=2000, null=False)
    writer = models.CharField(max_length=255, null=False)
    content = models.TextField(max_length=200000, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    coverImg = models.ImageField(null=False)
    createdAt = models.DateTimeField(auto_now_add=True, null=False)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
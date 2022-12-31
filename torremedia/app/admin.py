from django.contrib import admin
from .models import Category
from .models import Article

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
  list_display = ("id", "name", "createdAt")
  
class ArticleAdmin(admin.ModelAdmin):
  list_display = ("id", "title", "description", "writer", "content", "category", "coverImg", "createdAt", "updatedAt")
  
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
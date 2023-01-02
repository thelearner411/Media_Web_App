from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('helloworld', views.helloWorld, name='helloworld'),
    path('categories/', views.categories, name='categories'),
    path('categories/browse/all', views.browseall, name='browseall'),
    path('categories/browse/<int:id>', views.browse, name='browse'),
    path('article/<int:id>', views.article, name='article'),
    path('testing/', views.testing, name='testing'),
]
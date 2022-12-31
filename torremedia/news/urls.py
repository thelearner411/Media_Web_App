from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('helloworld', views.helloWorld, name='helloworld'),
    path('categories/', views.news, name='news'),
    path('categories/browse/<int:id>', views.browse, name='browse'),
    path('testing/', views.testing, name='testing'),
]
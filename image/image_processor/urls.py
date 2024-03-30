
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static
from django.urls import path
from .views import index, result

urlpatterns = [
    path('', index, name='index'),
    path('result/', result, name='result'),
]

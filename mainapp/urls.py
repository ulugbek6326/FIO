from django.urls import path
from .views import fio

urlpatterns =[
    path('', fio, name='fio'),
]
from django.contrib import admin
from django.urls import path

from .views import Index, result_table, all_table

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('table/<str:id>/', result_table, name='table'),
    path('all/', all_table, name='all_table')
]

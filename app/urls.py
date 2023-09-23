from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name="home"),
    path('view_data/',view_data),
    path('download_file/<int:file_id>',download_file, name="download_file"),
    path('view_file/<int:file_id>',view_file, name="view_file"),
]
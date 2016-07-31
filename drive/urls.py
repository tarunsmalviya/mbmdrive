from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mydrive, name='mydrive'),
    url(r'^delete_drive_file/$', views.delete_drive_file, name='delete_drive_file'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('gallery/approve', views.approve, name='approve'),
    path('gallery/upload_photo', views.upload_photo, name='upload_photo')
]
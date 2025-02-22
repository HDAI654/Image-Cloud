from django.urls import path
from .views import *

urlpatterns = [
    path('upload', filechooser, name='filechooser'),
    path('saver', saver, name='saver'),
    path('Cloud/', show_images, name='show_images'),
]

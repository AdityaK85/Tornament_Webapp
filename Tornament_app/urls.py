from  django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('createRoom', create_room)
]
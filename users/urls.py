from django.urls import re_path as url
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', UserManager),
    # path('signal', SignalView),
]

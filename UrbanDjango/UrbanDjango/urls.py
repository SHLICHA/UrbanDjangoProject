from django.contrib import admin
from django.urls import path

from task2.views import index, index2
#from task3.views import games, cart, Platform
from task4.views import games, cart, Platform

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('index', index2.as_view()),
    path('platform/', Platform.as_view()),
    path('platform/games/', games),
    path('platform/cart/', cart)
]

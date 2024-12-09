from django.contrib import admin
from django.urls import path

from task2.views import index, index2
#from task3.views import games, cart, Platform
from task4.views import games, cart, Platform
from task5.views import sign_up_by_django, sign_up_by_html


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sign_up_by_html),
    path('django_sign_up', sign_up_by_django)
    #path('index', index2.as_view()),
    #path('platform/', Platform.as_view()),
    #path('platform/games/', games),
    #path('platform/cart/', cart)
]

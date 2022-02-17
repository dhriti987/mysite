from django.urls import path

from .views import index,home, result

urlpatterns = [
    path('',index),
    path('payal/',home),
    path('result/',result),
]
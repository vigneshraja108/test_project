from django.urls import path
from .views import user,user_data

urlpatterns = [
    path('', user, name="user"),
    path('get/', user_data, name="user_data"),


]

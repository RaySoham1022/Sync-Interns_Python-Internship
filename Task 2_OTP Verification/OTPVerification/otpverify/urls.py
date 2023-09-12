from django.urls import path

from . import views

app_name = "otpverify"
urlpatterns = [
    path('', views.index, name='index'),
]
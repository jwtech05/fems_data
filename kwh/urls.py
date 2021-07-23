from django.contrib import admin
from django.urls import path, include
from .views import addFemsTransData1,addFemsTransData2

urlpatterns = [
    path('temp/monitor/', addFemsTransData1.as_view()),
    path('kwh/monitor/', addFemsTransData2.as_view())
]

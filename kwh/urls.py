from django.contrib import admin
from django.urls import path, include
from .views import addFemsTransData

urlpatterns = [
    path('temp/monitor/', addFemsTransData.as_view()),
]

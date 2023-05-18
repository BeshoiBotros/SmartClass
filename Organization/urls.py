from django.urls import path
from .views import *
urlpatterns = [
    path('create-doctor/', createDoctorView, name='create-doctor')
]

from django.urls import path
from .views import *
urlpatterns = [
    path('create-doctor/', CreateDoctorView.as_view(), name='create-doctor'),
    path('show-doctors/', ViewDoctorsView.as_view(), name='view-doctors'),
    path('delete-doctor/<int:pk>/', deleteDoctor, name='delete-doctor')
]


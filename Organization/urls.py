from django.urls import path
from .views import *
urlpatterns = [
    path('create-doctor/', createDoctorView, name='create-doctor'),
    path('show-doctors/', viewDoctors, name='view-doctors'),
    path('delete-doctor/<int:id>/', deleteDoctor, name='delete-doctor')
]
 
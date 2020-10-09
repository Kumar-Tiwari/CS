from django.urls import path
from .views import users_data
urlpatterns = [
    path('',users_data),
    
]
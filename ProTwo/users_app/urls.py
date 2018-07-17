from django.urls import path
from users_app import views

urlpatterns = [
    path('', views.users, name='users')
]

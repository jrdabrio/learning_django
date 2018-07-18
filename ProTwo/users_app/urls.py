from django.urls import path
from users_app import views

urlpatterns = [
    path('', views.users, name='users'),
    path('signup/', views.sign_up, name='sign_up'),
]

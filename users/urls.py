"""
URL mappings for the user API.
"""
from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('', views.CreateUserView.as_view(), name='users'),
    path('<int:pk>/', views.ManageUserView.as_view(), name='user-detail')

]

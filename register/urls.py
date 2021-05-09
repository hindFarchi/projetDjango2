from django.urls import path

from . import views

app_name = 'register'

urlpatterns = [
    path('', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout')
]

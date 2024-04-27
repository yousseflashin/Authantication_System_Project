from django.urls import path

from . import views
urlpatterns = [
    path('',views.registerView,name='register'),
    path('login/',views.loginView,name='login'),
    path('profile/',views.profileView,name='profile'),
    path('logout/',views.logoutView,name='logout'),
]

from django.urls import path

from user import views

app_name='user'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.user, name='profile'),
    path('profile_update/', views.update_user, name='profile_update'),
    path('avatar/load', views.avatar_load, name='avatar-load'),
]
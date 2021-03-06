from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup_pg/', views.signup_pg, name='signup_pg'),
    path('login_pg/', views.login_pg, name='login_pg'),
    path('re_login/', views.login, name='re_login'),
    path('home/', views.home_view, name='home_view'),
]
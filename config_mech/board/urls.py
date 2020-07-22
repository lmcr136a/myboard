from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('new/', views.new_post, name='new_post'),
    path('<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>', views.delete_post, name='delete_post'),
]
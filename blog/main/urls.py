from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
	path('post/<int:pk>/delet/', views.post_delet, name='post_delet'),
	path('post/new/', views.post_new, name='post_new'),
]
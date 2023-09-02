from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view/<int:post_id>/', views.view_post, name='view_post'),
    path('create/', views.create_post, name='create_post'),
]

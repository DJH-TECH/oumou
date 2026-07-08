from django.urls import path

from . import views

app_name = 'siteweb'

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.posts_list, name='post_list'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
]

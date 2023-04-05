from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_posts, name='show_posts'),
    path('<int:post_id>/', views.post_details, name='post_details'),
]


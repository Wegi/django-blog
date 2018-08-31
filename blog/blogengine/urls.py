from django.urls import path
from blogengine import views

app_name = "blogengine"

urlpatterns = [
    path('posts/', views.all_posts, name="posts.all")
]
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostList.as_view(), name="posts"),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name="lonePost"),
]

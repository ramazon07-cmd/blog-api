from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name="posts"),
    path('<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('create/', PostCreateView.as_view(), name="post_create"),
    path('update/<int:pk>/', PostUpdateView.as_view(), name="post_update"),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name="post_delete"),
]

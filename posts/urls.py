from django.urls import path
from .views import PostList, PostAdd, PostDetail, PostUpdate, PostDelete

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/add/', PostAdd.as_view(), name='post-add'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('posts/<int:pk>/update/', PostUpdate.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDelete.as_view(), name='post-delete'),
]

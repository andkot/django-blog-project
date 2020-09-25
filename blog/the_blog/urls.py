from django.urls import path
from .views import HomeView, ArticleDetailsView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailsView.as_view(), name='article details'),
    path('add_post', AddPostView.as_view(), name='add post'),
    path('article/update/<int:pk>', UpdatePostView.as_view(), name='update post'),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name='delete post'),
]

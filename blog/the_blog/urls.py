from django.urls import path
from .views import HomeView, ArticleDetailsView, AddPostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailsView.as_view(), name='article details'),
    path('add_post', AddPostView.as_view(), name='add post'),
]

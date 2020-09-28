from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailsView.as_view(), name='article details'),
    path('add_post', AddPostView.as_view(), name='add post'),
    path('add_category', AddCategoryView.as_view(), name='add category'),
    path('article/update/<int:pk>', UpdatePostView.as_view(), name='update post'),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name='delete post'),
    path('categories', CategoriesView.as_view(), name='categories'),
    path('categories/<int:pk>', get_posts_with_category, name='posts with category')
]

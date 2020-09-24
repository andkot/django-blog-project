from django.urls import path
from .views import HomeView, ArticleDetailsView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailsView.as_view(), name='article details'),
]

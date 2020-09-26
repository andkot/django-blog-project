from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm, CategoryForm
from django.urls import reverse_lazy
from django.shortcuts import render


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['creating_date']


def get_posts_with_category(request, category_name):
    posts_with_category = Post.objects.filter(category=category_name)
    return render(request, 'posts_with_category.html',
                  {'posts_with_category': posts_with_category, 'category_name': category_name})


class CategoriesView(ListView):
    model = Category
    template_name = 'categories.html'


class ArticleDetailsView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'add_category.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

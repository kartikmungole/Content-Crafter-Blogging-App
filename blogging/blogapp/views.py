from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# ListView for displaying all posts
class PostListView(ListView):
    model = Post
    template_name = 'blogs/post_list.html'
    context_object_name = 'posts'

# DetailView for displaying a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blogs/post_details.html'

# CreateView for creating a new post
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blogs/post_forms.html'
    success_url = reverse_lazy('post-list')


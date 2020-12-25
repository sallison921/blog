from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
# def home(request):
#     return render(request, 'home.html',{})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class AllPostsView(ListView):
    model = Post
    template_name = 'allPosts.html'

class AboutView(ListView):
    model = Post
    template_name = 'about.html'

class ArticleView(DetailView):
    model = Post
    template_name = "articlePages.html"

class AddPostView(CreateView):
    model = Post
    template_name = "addPost.html"
    fields = "__all__"

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'updatePost.html'
    fields = ['title', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'deletePost.html'
    success_url = reverse_lazy("allPosts") 
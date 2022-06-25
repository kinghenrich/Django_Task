from dataclasses import fields
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.edit import ListView
from django.views.generic.edit import DetailView
from .models import Post



class blogPostCreateView(CreateView):
    model = Post
    fields="__all__"
    success_url = reverse_lazy("blog:all")

    class blogPostListView(ListView):
     model = Post

    class blogPostDetailView(CreateView):
        model = Post

class blogPostUpdateView(UpdateView):
    model = Post
    fields="__all__"
    success_url = reverse_lazy("blog:all")

class blogPostDeleteView(DeleteView):
    model = Post
    fields="__all__"
    success_url = reverse_lazy("blog:all")         
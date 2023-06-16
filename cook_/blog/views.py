from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__tag=self.kwargs.get("tag")).select_related('category')

def home(request):
    return render(request, 'base.html')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

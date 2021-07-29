from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Post


class HomeView(ListView):
    pass


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        # Возраащает посты отфилтьрованые по слагу и категриям
        # self.kwargs.get('slug')) slug - это название которое обзначено в url.py
        return Post.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'


def home(request):
    return render(request, 'base.html')
from django.views.generic import ListView, DetailView

from .models import Post


class HomeView(ListView):
    model = Post
    paginate_by = 9
    template_name = 'blog/home.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        # Возраащает посты отфилтьрованые по слагу и категриям
        # self.kwargs.get('slug')) slug - это название которое обзначено в url.py
        return Post.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')


class PostDetailView(DetailView):
    model = Post
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

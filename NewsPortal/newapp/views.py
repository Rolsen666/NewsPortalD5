from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from .models import Post, Author
from .filters import PostFilter
from .forms import PostForm, ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class PostNewsList(ListView):
    model = Post
    ordering = ['-dateCreation']
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 2  # Тут 2 потому что всего 4 публикации
    form_class = PostForm


class Post_Filter(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'news'
    #queryset = Post.objects.all()


class PostCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'add.html'
    form_class = PostForm
    permission_required = ('newapp.add_post',)


class PostUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'edit.html'
    form_class = PostForm
    permission_required = ('newapp.change_post',)

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'profile_update.html'
    form_class = ProfileUpdateForm
    success_url = 'news/'

    def get_object(self, **kwargs):
        return self.request.user


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    context_object_name = 'news'
    success_url = '/news/'

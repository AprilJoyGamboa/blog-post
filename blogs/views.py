from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from blogs.forms import *
from blogs.models import *

# Create your views here.
class BlogPostIndexView(ListView):
    model = BlogPost
    template_name = 'index.html'
    context_object_name = 'blog_posts'
    paginate_by = 10

class AuthorListView(ListView):
    model = Author
    template_name = 'author-list.html'
    context_object_name = 'authors'
    paginate_by = 10

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author-detail.html'
    context_object_name = 'author'

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author-create.html'
    success_url = '/authors/'

class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author-update.html'
    success_url = '/authors/'
    context_object_name = 'author'

class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author-delete.html'
    success_url = '/authors/'
    context_object_name = 'author'

class CategoryListView(ListView):
    model = Category
    template_name = 'category-list.html'
    context_object_name = 'categories'
    paginate_by = 10

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category-detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category-create.html'
    success_url = '/categories/'

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category-update.html'
    success_url = '/categories/'
    context_object_name = 'category'

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category-delete.html'
    success_url = '/categories/'
    context_object_name = 'category'

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog-post-list.html'
    context_object_name = 'blog_posts'
    paginate_by = 10

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog-post-detail.html'
    context_object_name = 'blog_post'

class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog-post-create.html'
    success_url = '/blog_posts/'

    def form_valid(self, form):
        form.instance.author = self.request.user.author
        return super().form_valid(form)

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog-post-update.html'
    success_url = '/blog_posts/'
    context_object_name = 'blog_post'

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog-post-delete.html'
    success_url = '/blog_posts/'
    context_object_name = 'blog_post'

def blog_post_detail(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog-post-detail.html', {'blog_post': blog_post})

class RegistrationView(View):
    template_name = 'register.html'

    def get(self, request):
        form = AuthorForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthorForm(request.POST)
        if form.is_valid():
            user = form.save().user
            login(request, user)
            return redirect('index')
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        return render(request, self.template_name, {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', BlogPostIndexView.as_view(), name='index'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('authors/create/', AuthorCreateView.as_view(), name='author-create'),
    path('authors/update/<int:pk>', AuthorUpdateView.as_view(), name='author-update'),
    path('authors/delete/<int:pk>', AuthorDeleteView.as_view(), name='author-delete'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/update/<int:pk>', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/delete/<int:pk>', CategoryDeleteView.as_view(), name='category-delete'),
    path('blog_posts/', BlogPostListView.as_view(), name='blogpost-list'),
    path('blog_posts/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost-detail'),
    path('blog_posts/create/', BlogPostCreateView.as_view(), name='blogpost-create'),
    path('blog_posts/update/<int:pk>', BlogPostUpdateView.as_view(), name='blogpost-update'),
    path('blog_posts/delete/<int:pk>', BlogPostDeleteView.as_view(), name='blogpost-delete'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
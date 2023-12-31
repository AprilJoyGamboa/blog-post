import os
import sys
import django
from django.core.wsgi import get_wsgi_application
from django.contrib.auth.models import User
from blogs.models import *
from blogs.forms import *
import random

# script_path = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.join(script_path, 'projectsite'))
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectsite.settings')
# django.setup()

def create_superuser():
    username = 'admin'
    password = 'pass'
    email = 'admin@yahoo.com'
    user = User.objects.create_superuser(username=username, password=password, email=email)
    return user


# Function to create sample users
def create_sample_users():
    users = []
    for i in range(1, 21):
        username = f'user{i}'
        password = f'password{i}'
        user = User.objects.create(username=username, password=password)
        users.append(user)
    return users

# Function to create sample authors
def create_sample_authors():
    authors = []
    for i in range(1, 21):
        author_name = f'Author {i}'
        author = Author.objects.create(name=author_name)
        authors.append(author)
    return authors

# Function to create sample categories
def create_sample_categories():
    categories = []
    category_titles = ['Technology', 'Science', 'Travel', 'Food and Cooking', 'Health and Fitness', 'Fashion', 'Business and Finance', 'Arts and Culture', 'Lifestyle', 'Personal Development', 'Gaming', 'Literature', 'Sports', 'Music', 'Photography']
    for title in category_titles:
        category = Category.objects.create(title=title)
        categories.append(category)
    return categories

# Function to generate sample content for blog posts
def generate_sample_content():
    sample_content = [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
        "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    ]
    return random.choice(sample_content)

# Function to create sample blog posts
def create_sample_blogposts(authors, categories):
    blogposts = []
    for i in range(1, 21):
        title = f'Blog Post {i} - {random.choice(["Exciting", "Thought-Provoking", "Informative"])}'
        content = generate_sample_content()
        author = authors[i - 1]
        category = categories[i % len(categories)]
        blogpost_data = {'title': title, 'content': content, 'author': author, 'categories': [category]}
        blogposts.append(blogpost_data)
    return blogposts

# Main script
superuser = create_superuser()
print(f'superuser created...')
# sample_users = create_sample_users()
# sample_authors = create_sample_authors()
# sample_categories = create_sample_categories()
# sample_blogposts = create_sample_blogposts(sample_authors, sample_categories)

# for data in sample_blogposts:
#     form = BlogPostForm(data)
#     if form.is_valid():
#         blog_post = form.save(commit=False)
#         blog_post.author = data['author']
#         blog_post.save()
#         form.save_m2m()
#         print(f"BlogPost '{blog_post.title}' created successfully.")
#     else:
#         print(f"Error creating BlogPost: {form.errors}")

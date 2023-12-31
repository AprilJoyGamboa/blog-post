from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Author(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(BaseModel):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class BlogPost(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='blog_images', null=True, blank=True)

    def __str__(self):
        return self.title

class Comment(BaseModel):
    text = models.TextField()
    author = models.CharField(max_length=100)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} - {self.text[:50]}"


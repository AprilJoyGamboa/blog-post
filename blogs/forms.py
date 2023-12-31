from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from blogs.models import *

class AuthorForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = Author
        fields = ['bio', 'name']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )

        author = super(AuthorForm, self).save(commit=False)
        author.user = user

        if commit:
            user.save()
            author.save()

        return author

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']

class BlogPostForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'categories', 'image']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    
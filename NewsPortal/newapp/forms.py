from django.forms import ModelForm
from .models import Post
from django.contrib.auth.models import User


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'author',
                  'categoryType', 'text',
                  ]


class ProfileUpdateForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']

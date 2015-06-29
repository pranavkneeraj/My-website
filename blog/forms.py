
from django import forms

from .models import Post

from .models import Login

import re
from custom_user.models import AuthUser
from django.utils.translation import ugettext_lazy as _

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class LoginForm(forms.ModelForm):

    class Meta:
        model = Login
        fields = ('username', 'password',)





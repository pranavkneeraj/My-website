import uuid
from django.db import models
from django.core.context_processors import csrf
from django.core.mail import send_mail
from .models import Post
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Login
from django.contrib.auth import logout
from .forms import PostForm
from .forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import hashlib, datetime, random
from custom_user.models import UserActivationProfile

from django.shortcuts import redirect,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from blog.forms import *
from custom_user.forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.template import RequestContext

def post_list(request):
    posts = Post.objects.all();	
    if request.path=='/pranav':
   	 			return render(request, 'blog/post_list1.html', {'request': request,'posts':posts});	
    else :
			        return render(request, 'blog/post_list.html', {'request': request,'posts':posts});
def logout_view(request):
    logout(request)
    posts = Post.objects.all();
    return render(request,'blog/post_list.html',{'posts':posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def register(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active=False
            user.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            email_subject = 'Account confirmation'
            activation_key=str(uuid.uuid4());
            key_expires = datetime.datetime.today() + datetime.timedelta(2)
            user=AuthUser.objects.get(username=username)
            new_profile = UserActivationProfile(user=user, activation_key=activation_key,
                                                      key_expires=key_expires)
            new_profile.save()
            email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \
            48hours http://127.0.0.1:8000/accounts/confirm/%s" % (username, activation_key)
            
            send_mail(email_subject, email_body, 'pranavkchaudhary@gmail.com.com',
                      [email], fail_silently=False)
            
            return HttpResponseRedirect('/register/success/')
    else:
        form=RegistrationForm();
    return render(request,'blog/registration.html',{'form':form})

def register_confirm(request, activation_key):
    user_profile = get_object_or_404(UserActivationProfile, activation_key=activation_key)
    user = user_profile.user
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    if user.is_active:
        return render(request, 'blog/post_list.html', {})   
        
        # check if there is UserProfile which matches the activation key (if not then display 404)
   
    
        #check if the activation key has expired, if it hase then render confirm_expired.html
    if user_profile.key_expires < timezone.now():
        return render(request, 'blog/expire.html', {})   
        #if the key hasn't expired save user and set him as active and render some template to confirm activation
    
    user.is_active = True
    user.save()
    return render(request,'blog/confirm.html',{})


def register_success(request):
            return render_to_response(
                'blog/success.html',
            )
    


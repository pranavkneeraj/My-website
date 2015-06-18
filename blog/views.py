from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Login


from django.contrib.auth import logout
from .forms import PostForm
from .forms import LoginForm
from django.contrib.auth import authenticate


from django.shortcuts import redirect,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

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

def login(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
                    u=request.POST['username'];
                    p=request.POST['password'];
                    user = authenticate(username=u, password=p)
                    if user:
                        return redirect('blog.views.post_list')
	else:
		form = LoginForm()
	return render(request,'blog/login.html',{"form":form});



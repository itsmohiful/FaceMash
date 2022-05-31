from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm, PostForm
from .models import Post


#home
def home(request):
    posts = Post.objects.order_by('-posted_at')
    return render(request,'feed/home.html',{'posts':posts})


#create new post
@login_required(login_url='login')
def creat_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.post_author = request.user
            post.save()
            messages.success(request,'Post created successfully.')
            return redirect('/')
    context = {
        'forms' : form
    }

    return render(request,'feed/create_post.html',context)



#post detail view
def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    comments = post.comment_set.all()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.comment_autor = request.user
            comment.save()
            messages.success(request,'Comment added successfully.')
    
    else:
        form = CommentForm()

    context = {
        'post' : post,
        'form' : form,
        'comments': comments,
    }

    return render(request,'feed/post_detail.html',context)


#edit post 
login_required(login_url='logoin')
def edit_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(instance = post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            form.save()
            messages.success(request,'Post updated successfully.')
            return redirect('/')

    context = {
        "form" : form
    }

    return render(request,'feed/edit_post.html',context)


#delete post
@login_required(login_url='login')
def delete_post(request,pk):
    post = get_object_or_404(Post,pk=pk)

    post.delete()
    # if request.method == 'POST':
    #     post.delete()
    #     return redirect('/')
    # context = {
    #     'post' : post
    # }

    # return render(request,'feed/delete_post.html',context)

    messages.success(request,"Post deleted successfully.")


def test(request):
    pass

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post


#home
def home(request):
    posts = Post.objects.order_by('-posted_at')
    return render(request,'feed/home.html',{'posts':posts})


#create new post
def creat_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request,'Post created successfully.')
            return redirect('/')
    context = {
        'forms' : form
    }

    return render(request,'feed/create_post.html',context)



#post detail view
def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    context = {
        "post" : post
    }

    return render(request,'feed/post_detail.html',context)


#edit post 
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

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm, PostForm
from .models import Comment, Post


#home
def home(request):
    posts = Post.objects.order_by('-posted_at')
    paginator = (Paginator(posts,3))
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    if request.method == 'POST':
        search = request.POST.get('search')
        #results = Post.objects.filter(Q(title__icontains=search))
        results = Post.objects.filter(Q(title__icontains=search) | Q(description__icontains=search))
        context =  { 
            'results': results
        }
        return render(request, 'feed/search_result.html', context)

    context = {
        'posts' : posts,
    }

    return render(request,'feed/home.html',context)


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
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.comment_author = request.user
            comment.save()
            messages.success(request,'Comment added successfully.')

            context = {
                'post' : post,
                'form' : form,
                'comments': comments,
            }
            return render(request,'feed/post_detail_after_comment.html',context)
    
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

    # post.delete()
    if request.method == 'POST':
        post.delete()
        messages.success(request,"Post deleted successfully.")
        return redirect('/')

    context = {
        'post' : post
    }

    
    return render(request,'feed/delete_post.html',context)

    


login_required(login_url='logoin')
def edit_comment(request,pk):
    comment = get_object_or_404(Comment, pk=pk)
    form = CommentForm(instance = comment)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance = comment)
        if form.is_valid():
            form.save()
            messages.success(request,'comment updated successfully.')
            return redirect('/')

    context = {
        "form" : form
    }

    return render(request,'feed/edit_comment.html',context)



login_required(login_url='logoin')
def delete_comment(request,pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        comment.delete()
        messages.success(request,'comment deleted successfully.')
        return redirect('/')


    return render(request,'feed/edit_comment.html')

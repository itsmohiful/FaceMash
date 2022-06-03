from multiprocessing import context

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from feed.models import Post

from .forms import ProfileUpdateForm, RegisterForm, UserUpdateForm
from .models import Profile


#registration view
def register(request):

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            messages.success(request,f'Account has been created for {username}')
            return redirect('login')
    
    else:
        register_form = RegisterForm()

    context = {
        'form' : register_form
    }

    return render(request,'users/register.html',context)


#Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'login successfully')
            return redirect('home')

        else:
            messages.error(request,"Invalid credentials")

    return render(request,'users/login.html')


#Logout view
def logout_view(request):
    logout(request)
    return redirect('login')



#user profile view
# def profile(request,username):
#     user_id = User.objects.filter(username=username)
#     posts = Post.objects.filter(post_author__username=user_id)
#     print('user===',user_id)
#     #print('post===',posts)
#     context = {
#         'posts' : posts,
#     }
#     return render(request,'users/profile.html')


class UserProfileListView(ListView):
    model = Post
    template_name = 'users/profile.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(post_author=user).order_by('-posted_at')


class UserPostListView(ListView):
    model = Post
    template_name = 'users/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(post_author=user).order_by('-posted_at')


#profile update
def update_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance = request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        if user_form.is_valid() or profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request,f'your profile has been updated')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance = request.user)
        profile_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'user_form' : user_form,
        'profile_form' : profile_form
    }


    return render(request,'users/profile_update.html',context)

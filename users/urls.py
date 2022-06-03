from unicodedata import name

from django.urls import path

from . import views
from .views import UserPostListView, UserProfileListView

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    #path('<str:username>/profiles',views.profile, name='profile'),
    path('<str:username>/profiles', UserProfileListView.as_view(), name='profile'),
    path('<str:username>/posts', UserPostListView.as_view(), name='user-posts'),
    path('profile/update',views.update_profile, name='update_profile'),
]

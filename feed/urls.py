from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('creat-post/',views.creat_post, name="creat-post"),
    path('post/<int:pk>/detail',views.post_detail, name="post-detail"),
    path('post/<int:pk>/edit',views.edit_post, name="edit-post"),
    path('post/<int:pk>/delete',views.delete_post, name="delete-post"),
    path('comment/<int:pk>/edit',views.edit_comment, name="edit-comment"),
    path('comment/<int:pk>/delete',views.delete_comment, name="delete-comment"),
]

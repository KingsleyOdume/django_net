from django.urls import path
from .views import PostListView
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-newsfeed'),
    path('timeline/', views.timeline, name='blog-timeline'),
    path('faq/', views.faq, name='blog-faq'),
    path('timeline_about/', views.timeline_about, name='blog-timeline_about'),
    path('timeline_album/', views.timeline_album, name='blog-timeline_album'),
    path('timeline_friends/', views.timeline_friends, name='blog-timeline_friends'),
    path('newsfeed_images/', views.newsfeed_images, name='blog-newsfeed_images'),
    path('home/', views.home, name='blog-home'),
    path('comments/', views.comment, name='blog-comment'),
    path('comment/', views.create_comment, name='blog-create_comment')
]

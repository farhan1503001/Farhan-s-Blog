from blog_app.views import AboutView, PostView
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path(r'^about/$',AboutView.as_view,name='about'),
    path(r'^$',views.PostView.as_view,name='post_list'),
    path(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view,name='post_detail'),
    path(r'^post/new/$',views.PostCreateView.as_view,name='post_create'),
    path(r'^post/(?P<pk>\d+)/update/$',views.PostUpdateView.as_view,name='post_update'),
    path(r'^post/(?P<pk>\d+)/delete/$',views.PostDeleteView.as_view,name='post_delete'),
    path(r'^draft/$',views.PostDraftView.as_view,name='draft_view'),
    path(r'^post/(?P<pk>\d+)/comment/$',views.add_comment,name='add_comment'),
    path(r'^comment/(?P<pk>\d+)/approve/$',views.approve_comment,name='approve_comment'),
    path(r'^comment/(?P<pk>\d+)/remove/$',views.approve_comment,name='comment_remove'),
    path(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name='publish_post')

]
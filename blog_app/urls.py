from blog_app.views import AboutView, PostView
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path(r'^about/$',AboutView.as_view,name='about'),
    path(r'^$',views.PostView.as_view,name='post_list'),
    path(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view,name='post_detail')
]
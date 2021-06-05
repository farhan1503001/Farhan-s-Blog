from django.shortcuts import render
from django.utils import timezone
from blog_app.models import Post,Comment
from blog_app.forms import CommentForm,PostForm
from django.views.generic import (TemplateView,ListView,DetailView)
# Create your views here.
class AboutView(TemplateView):
    template_name='about.html'

#Now template for showing all the posts present
class PostView(ListView):
    model=Post

    def get_queryset(self):
        return Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')

#Now template for viewing specific post
class PostDetailView(DetailView):
    model=Post
#Now template for 


from django.contrib.auth import mixins
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse_lazy
from django.utils import timezone
from django.views.generic.edit import DeleteView
from blog_app import forms
from blog_app.models import Post,Comment
from blog_app.forms import CommentForm,PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
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
#Now template for createview but we have to ensure the creator has logged in
class PostCreateView(CreateView,LoginRequiredMixin):
    login_url='/login/' #Address to the login page
    redirect_field_name='blog_app/post_detail.html' # After creating where the move will occured

    model=Post
    form_class=PostForm

#Now template for updating view here it is also required that user is logged in
class PostUpdateView(UpdateView,LoginRequiredMixin):
    login_url='/login/'
    redirect_field_name='blog_app/post_detail.html'
    
    model=Post
    form_class=PostForm

#Now template class for deleting entry
class PostDeleteView(DeleteView,LoginRequiredMixin):
    login_url='/login/'
    success_url=reverse_lazy('post_list')

#Now template class for draft viewing
class PostDraftView(ListView,LoginRequiredMixin):
    login_url='/login/'
    redirect_field_name='blog_app/post_list.html'
    model=Post

    def get_queryset(self):
        return Post.objects.filter(publish_date__isnull=True).order_by('-creation_date')

#Now publishing the post
@login_required
def post_publish(request,pk=pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_details',pk=pk)

#########################################################################################################################
#.......................................Comment Section................................................................#
#################################################################################################################
@login_required
def add_comment(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('post_detail',pk=post.pk,{'form':form})
    else:
        form=CommentForm()
        return render(request,'blog/comment_form.html')

@login_required
def approve_comment(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.approve_status()
    return redirect('post_detail')
@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    post_pk=comment.post.pk
    return redirect('post_details',pk=post_pk)

from datetime import timedelta
from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()
    creation_date=models.DateTimeField(default=timezone.now())
    publish_date=models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.publish_date=timezone.now()
        self.save()
    #Now for holding comment with post
    def display_approved_comments(self):
        self.comments.filter(status=True)
    #Now we have to decide how to display the post after writing it
    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    #Now creating relation between these two models
    post=models.ForeignKey('blog_app.Post',related_name='comments')
    author=models.CharField(max_length=200)
    comment=models.TextField()
    create_date=models.DateTimeField(default=timezone.now())
    status=models.BooleanField(default=False)

    def approve_status(self):
        self.status=True
        self.save()
    def get_absolute_url(self):
        return reverse('post_list')
    def __str__(self):
        return self.author

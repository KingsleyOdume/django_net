from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class MyPost(models.Model):
    pic = models.ImageField(upload_to='profile_pics', null=True)
    video = models.ImageField(upload_to='profile_pics', null=True)
    subject = models.CharField(max_length=200)
    msg = models.TextField(null=True, blank=True)
    cr_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.subject

    def get_absoulte_urls(self):
        return reverse('blog-newsfeed')


class Comment(models.Model):
    comment = models.TextField(null=True, max_length=1000)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

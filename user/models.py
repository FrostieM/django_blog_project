from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey('self', related_name='comments', on_delete=models.CASCADE, null=True, blank=True)
    publication_date = models.DateTimeField(auto_now=True)


def upload_to_user_folder(instance, filename):
    src = instance.type or 'image'
    return f"{instance.blog.user.username}/{src}/{filename}"


class Blog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile = models.ImageField(upload_to=upload_to_user_folder, height_field=None, width_field=None)
    created = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    title = models.CharField(max_length=60)
    description = models.TextField()
    file = models.FileField(upload_to=upload_to_user_folder, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now_add=True)


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

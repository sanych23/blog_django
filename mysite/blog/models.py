from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "auth_user"


class CategoryPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    keywords = models.TextField(null=True)


class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # category = models.CharField(max_length=100)
    post_date = models.DateField(auto_created=True)
    image_path = models.CharField(max_length=255)
    category = models.ForeignKey("CategoryPost", on_delete=models.DO_NOTHING, null=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    view_count = models.PositiveIntegerField(default=0)

    def countComment(self):
        return Comment.objects.filter(post=self).count()


# class Author(models.Model):
#     name = models.CharField(max_length=100)


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey("Posts", on_delete=models.DO_NOTHING, null=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)

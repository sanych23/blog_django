from django.db import models


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
    author = models.ForeignKey("Author", on_delete=models.DO_NOTHING, null=True)
    view_count = models.PositiveIntegerField(default=0)

    def countComment(self):
        return Comment.objects.filter(post=self).count()


class Author(models.Model):
    name = models.CharField(max_length=100)


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey("Posts", on_delete=models.DO_NOTHING, null=True)
    author = models.ForeignKey("Author", on_delete=models.DO_NOTHING, null=True)
    comment_date = models.DateField(auto_created=True)


class Localization(models.Model):
    type = models.CharField(max_length=50)

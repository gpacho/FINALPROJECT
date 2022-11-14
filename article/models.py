from django.db import models

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    content_upload = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)

class Comment(models.Model):
    product = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
    commenter_name = models.CharField(max_length=200)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.product.title, self.commenter_name)
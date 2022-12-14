from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, db_index=True,verbose_name="Url")
    content = models.TextField()
    photo = models.ImageField(upload_to="photo/%Y/%m/%d")
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    cat = models.ManyToManyField('Category')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_page', kwargs={'post_slug': self.slug})

    class Meta:
        ordering = ["time_created","title"]


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(unique=True, db_index=True, verbose_name="Url")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})




class Comment(models.Model):
    content = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,related_name="users",on_delete=models.CASCADE)
    post = models.ForeignKey('Post',related_name="comments", on_delete=models.CASCADE)
    def __str__(self):
        return '%s - %s' % (self.post.title,self.user.username)

    class Meta:
        ordering = ["time_created",]


from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse('user:home')


class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextField(blank=True, null=True)
    title_tag = models.CharField(max_length=50)
    publish_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=40)
    likes = models.ManyToManyField(User, related_name="blog_likes")
    views = models.ManyToManyField(User, related_name="blog_views")
    snippet = models.TextField(max_length=100)

    class Meta:
        ordering = ['-publish_date']

    def total_likes(self):
        return self.likes.count()
    
    def total_views(self):
        return self.views.count()

    def publish(self):
        self.publish_date = timezone.now()

    def __str__(self):
        return f'{self.title} By {self.author.username}'
    
    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk':self.pk})
    
# class Comment(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time =  models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']


    def __str__(self):
        return f'{self.author.username} on {self.blog.title}'

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk':self.blog_id})
    

class UserProfile(models.Model):

    user = models.OneToOneField(User, related_name="profile",on_delete=models.CASCADE)

    # Adding additional feilds

    profile_pic = models.ImageField(blank=True,null=True,upload_to='images/profile')
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    description = models.TextField(max_length=250, blank=True)
     

    def __str__(self):
        return f'USER NAME: {self.user.username}'
    
    def get_absolute_url(self):
        return reverse('user:myProfile',kwargs={'user':self.user.username})
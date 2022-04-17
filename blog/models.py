from email.mime import image
from django.db import models
from django.utils.html import format_html
#from django.contrib.auth.models import User
#from tinymce.models import HTMLField
#
# from tinymce.models import HTMLField

# Create your models here.
class Category(models.Model):
    catid=models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    descriptions=models.TextField()
    url=models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    adddate=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.title
    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;"  />'.format(self.image))


class post(models.Model):
    postid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content = models.TextField()
    url=models.CharField(max_length=100)
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='post/')
    def __str__(self):
        return self.title



#self added comment model
# class Comment(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     date=models.DateField(auto_now_add=True)
#     post=models.ForeignKey('post',on_delete=models.CASCADE)
#     content=models.TextField()
#     def __str__(self):
#             return self.user.username    



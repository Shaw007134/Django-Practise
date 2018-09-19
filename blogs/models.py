from django.db import models
from django.contrib.auth.models import User
#from django.forms.models import model_to_dict
# Create your models here.

class BlogPost(models.Model):
    """博客主题，内容发布"""
    title = models.CharField(max_length=200)
    text = models.TextField()
    # blogs_cont = {'title': title, 'text': text }
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        """返回博客主题及文本"""
        return self.title
    
    
    


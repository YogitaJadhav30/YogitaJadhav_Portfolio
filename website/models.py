from django.db import models
from django.contrib.auth.models import User
from Blog.models import models


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject=models.CharField(max_length=200)
    message=models.TextField(max_length=500)
    
    def __str__(self):
        return self.name
    
STATUS={
    (0,'Draft'),
    (1,'Publish')
}
    
class Blogs(models.Model):
    title= models.CharField(max_length=100, unique=True)
    author= models.CharField(max_length=50)
    updated= models.DateTimeField(auto_now=True)
    content= models.TextField()
    created= models.DateTimeField(auto_now=True)
    status= models.IntegerField(choices=STATUS,default=0)
    
    class Meta:
        ordering = ['-created']
        
    def __str__(self):
        return self.title



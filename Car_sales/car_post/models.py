from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
# Create your models here.
class CarPosts(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    content= models.TextField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='uploads/', blank=True, null= True)
    def __str__(self):
        return f'{self.title}'
    
class Comment(models.Model):
    posts = models.ForeignKey(CarPosts, on_delete= models.CASCADE, related_name = 'comments')
    name = models.CharField(max_length= 50)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return f'Comment by{self.name}'
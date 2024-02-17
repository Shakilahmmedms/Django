from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length= 50)
    content = models.TextField()
    category = models.ManyToManyField(Category) #ekta categorir onk gulla post thakte parbe abar ekta post er onk gulla category thakte pare
    author = models.ForeignKey(User,on_delete= models.CASCADE)

    def __str__(self):
        return f'{self.title}'



from django.db import models
from Categories.models import Category
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length = 150)
    description = models.TextField()
    is_complete = models.BooleanField(default = False)
    task_date = models.DateField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
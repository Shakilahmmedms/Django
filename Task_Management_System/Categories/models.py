from django.db import models
# from Task.models import Task
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50)
    # task = models.ManyToManyField(Task)

    def __str__(self):
        return self.name
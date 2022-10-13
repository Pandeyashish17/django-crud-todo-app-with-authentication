from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class todoModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title=models.TextField()
    description=models.TextField()
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return f'({self.user} - {self.title} - {self.description} - {self.date})'











     
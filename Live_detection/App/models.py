from django.db import models
from django.contrib.auth.models import User
import time
# Create your models here.
class Display(models.Model):
    # user=models.ForeignKey(User, on_delete=models.CASCADE)
    array=models.JSONField()
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.array} - {self.updated}"



from django.db import models

# Create your models here.
class Display(models.Model):
    array=models.JSONField()
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.array} - {self.updated}"


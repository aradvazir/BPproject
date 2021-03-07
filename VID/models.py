from django.db import models

# Create your models here.
class teachvideos(models.Model):
    title=models.CharField(max_length=100)
    file=models.FileField(upload_to='vidfolder')

    def __str__(self):
       return self.title
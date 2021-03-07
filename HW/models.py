from django.db import models

# Create your models here.
class homework(models.Model):
    hw_title=models.CharField(max_length=100)
    hw_file=models.FileField(upload_to='hwfolder')

    def __str__(self):
        return self.title

class answer(models.Model):
    ans_title=models.CharField(max_length=100)
    student_nu=models.CharField(max_length=100)
    ans_file=models.FileField(upload_to='ansfolder')
    score=models.CharField(default='there is no score yet', max_length=100)
    date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


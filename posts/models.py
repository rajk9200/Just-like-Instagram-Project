from django.db import models
from datetime import date



# Create your models here.

class Posts(models.Model):
    image =models.FileField(upload_to='uploads', default='abcd')
    title =models.CharField(max_length=200)
    desc = models.TextField()
    date = models.DateField(default=date.today)


    def __str__(self):
        return self.title



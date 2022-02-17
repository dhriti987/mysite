from django.db import models

def create_path(instance,filename):
    return f'{instance.name}/{filename}'

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30,default='NoName')
    photo = models.ImageField(upload_to=create_path,default='hetvi.jpg')
    age = models.IntegerField()
    email = models.EmailField()
    DOB = models.DateField()

    def __str__(self):
        return self.name

from django.db import models

class teams (models.Model):
    title = models.CharField('Title', max_length=50)
    password = models.CharField('Pass', max_length=10)
    desc = models.CharField('Desc', null=True , max_length=300)
    pic = models.ImageField(upload_to= 'pictures/')
   
    objects = models.Manager()



def __str__(self):
        return self.title


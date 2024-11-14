from django.db import models

class teams (models.Model):
    title = models.CharField('Title', max_length=50)
    password = models.CharField('Pass', max_length=10)
    desc = models.CharField('Desc', null=True , max_length=300)
    pic = models.ImageField(upload_to= 'pictures/')
    #video = models.FileField(upload_to='videos/', null=True, blank=True) 
   



class drill (models.Model):
    title = models.CharField('Title', max_length=50)
    desc = models.CharField('Desc', null=True , max_length=500)
    pic = models.ImageField(upload_to= 'pictures/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True) 
    team= models.ForeignKey(teams, on_delete=models.CASCADE, null=True)
   
    

def __str__(self):
        return self.title

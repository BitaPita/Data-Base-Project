from django.db import models

class teams(models.Model):
    title = models.CharField('Title',max_length=30)
    desc = models.CharField('Desc',max_length=300,null=True)
    password= models.CharField('Pass',max_length=10)
    pic = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title


class drill(models.Model):
    title = models.CharField('Title', max_length=50)
    desc = models.CharField('Desc', null=True, max_length=500)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    team = models.ForeignKey(teams, on_delete=models.CASCADE, null=True)

class pic(models.Model):
    image = models.ImageField(upload_to='sd/')
    drill=models.ForeignKey(drill,on_delete=models.CASCADE,null=True,related_name='images')
class pos(models.Model):
    class Role(models.TextChoices):
        Pointguard  = "PG ", 'Pg '
        Shootingguard = "SG", 'Sg'
        Smallforward = "SF", 'Sf'
        Powerforward = "PF" ,'Pf'
        Center ="C",'c'
        others="OTHERS",'Others'
    position = models.CharField(max_length=50, choices=Role.choices)

class Strat(models.Model):
    title = models.CharField('Title', max_length=50)
    desc = models.CharField('Desc', null=True, max_length=500)
    team = models.ForeignKey(teams, on_delete=models.CASCADE, null=True)
    pos =models.ManyToManyField(pos, null=True,related_name='strategy')

class img(models.Model):
    image = models.ImageField(upload_to='si/')
    strat=models.ForeignKey(Strat,on_delete=models.CASCADE,null=True,related_name='images')


class diet(models.Model):
    class Meal(models.TextChoices):
        m1  = "D", 'Dinner'
        m2 = "B", 'Breakfast'
        m3 = "L", 'Lunch'
        m4 = "BG" ,'Pre Game'
        m5 ="AG",'Post Game'
        m6 ="S",'Snack'
    class Day(models.TextChoices):
        d1 = "S", 'Saturday'
        d2 = "SU", 'Sunday'
        d3 = "M", 'Monday'
        d4 = "T", 'Tuesday'
        d5 = "W", 'Wednesday'
        d6 = "TH", 'Thursday'
        d7 = "F", 'Friday'
    day = models.CharField(max_length=50, choices=Day.choices)
    meal = models.CharField(max_length=50, choices=Meal.choices)
    title = models.CharField('Title', max_length=50)
    desc = models.CharField('Desc', null=True, max_length=500)
    team = models.ForeignKey(teams, on_delete=models.CASCADE, null=True)

class news(models.Model):
    title = models.CharField('Title', max_length=100)
    desc = models.CharField('Desc', null=True, max_length=2000)
    pic = models.ImageField(upload_to='img/', null=True, blank=True)
    team = models.ForeignKey(teams, on_delete=models.CASCADE, null=True)
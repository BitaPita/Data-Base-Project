from django.db import models

from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models
from team.models import teams
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        PLAYER = "PLAYER", 'Player'
        COACH = "COACH", 'Coach'

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class playerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.PLAYER)


class Player(User):

    base_role = User.Role.PLAYER

    player = playerManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for students"


@receiver(post_save, sender=Player)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "PLAYER":
        playerProfile.objects.create(user=instance)


class playerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    height=models.IntegerField(null=True, blank=True)
    team = models.ForeignKey(teams, on_delete=models.CASCADE, null=True, )


class CoachManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.COACH)


class Coach(User):

    base_role = User.Role.COACH

    Coach = CoachManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for teachers"


class coachProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coach_id = models.IntegerField(null=True, blank=True)
    team = models.ForeignKey(teams, on_delete=models.CASCADE, null=True, )


@receiver(post_save, sender=Coach)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "COACH":
        coachProfile.objects.create(user=instance)
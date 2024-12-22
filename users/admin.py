from django.contrib import admin

from users.models import User,playerProfile,coachProfile

admin.site.register(User)
admin.site.register(playerProfile)
admin.site.register(coachProfile)
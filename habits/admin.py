from django.contrib import admin
from .models import Habit, Date, User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(User, UserAdmin)

admin.site.register(Habit)
admin.site.register(Date)
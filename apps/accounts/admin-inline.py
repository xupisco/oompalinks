from gamelib.accounts.models import *
from django.contrib import admin
from django.contrib.auth.models import User 
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)

class UsersInline(admin.TabularInline):
    fieldsets = (
        ("", {
            'fields': ('avatar', )
        }),
    )
    classes = ('collapse-closed', )
    model = UserProfile
    extra = 1
    
class UserOptions(UserAdmin):
    inlines = [UsersInline]

admin.site.register(User, UserOptions)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as RealUserAdmin
from django.contrib.auth.models import User
from apps.accounts.models import UserProfile

class UserProfileInline(admin.TabularInline):
    fieldsets = (
        ("", {
            'fields': ( )
        }),
    )
    allow_add = False
    
    model = UserProfile
    num_in_admin = 1
    min_num_in_admin = 1
    max_num_in_admin = 1
    num_extra_on_change = 0

class UserAdmin(RealUserAdmin):
    inlines = [ UserProfileInline ]
    
#admin.site.unregister(User)
#admin.site.register(User, UserAdmin)
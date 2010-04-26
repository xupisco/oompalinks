from apps.links.models import *
from django.contrib import admin

from django.utils.translation import ugettext as _

class LinkGroupOptions(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}


class LinkOptions(admin.ModelAdmin):
    list_display = ('c_owner', 'group', 'url', 'weight')
    
    def c_owner(self, obj):
        return obj.group.owner
    c_owner.short_description = _('owner')

admin.site.register(LinkGroup, LinkGroupOptions)
admin.site.register(Link, LinkOptions)
admin.site.register(Category)

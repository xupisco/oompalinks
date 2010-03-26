from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class UserProfile(models.Model):
    
    USER_CHOICES = (
        ('1', _('Producer')),
        ('2', _('Agency')),
        ('3', _('Client')),
        ('4', _('Guest')),
    )
    
    user = models.ForeignKey(User, unique=True)
    kind = models.CharField(_('kind'), blank=False, max_length=2, choices=USER_CHOICES, default='1')
    
def user_post_save(sender, instance, **kwargs):
    profile, new = UserProfile.objects.get_or_create(user=instance)
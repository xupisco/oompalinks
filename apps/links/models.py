# -*- coding: UTF-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from datetime import datetime

class LinkGroup(models.Model):
    owner = models.ForeignKey(User, verbose_name=_('onwer'))
    title = models.CharField(blank=True, max_length=128, verbose_name=_('title'))
    slug = models.SlugField(max_length=128, verbose_name=_('slug'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    sortable = models.BooleanField(default=False, verbose_name=_('sortable'))
    archived = models.BooleanField(default=False, verbose_name=_('archived'))
    date_added = models.DateField(default=datetime.today, verbose_name=_('date added'))

    def __unicode__(self):
         return self.title
         
    class Meta:
        ordering = ['date_added']
        verbose_name = _('group')
        verbose_name_plural = _('groups')


class Link(models.Model):
    group = models.ForeignKey(LinkGroup, verbose_name=_('group'))
    url = models.CharField(blank=False, max_length=255, verbose_name=_('url'))
    
    def __unicode__(self):
         return self.url
         
    class Meta:
        ordering = ['url']
        verbose_name = _('link')
        verbose_name_plural = _('links')
        
        
class Vote(models.Model):
    link = models.ForeignKey(Link)
    user = models.ForeignKey(User, verbose_name=_('user'))
    
    def __unicode__(self):
         return self.link
         
    class Meta:
        ordering = ['link']
        verbose_name = _('vote')
        verbose_name_plural = _('votes')
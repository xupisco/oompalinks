from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.links.models import *
import datetime

def main(request):
    latest = LinkGroup.objects.filter(archived = 0)[:10]
    return render_to_response('main.html', locals())
    

def group(request, slug):
    group = LinkGroup.objects.get(slug = slug)
    links = Link.objects.filter(group = group)
    return render_to_response('group.html', locals())
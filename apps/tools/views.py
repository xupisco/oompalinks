from django.shortcuts import HttpResponse
import datetime

def parseURL(request):
    from mechanize import Browser
    br = Browser()
    br.open(request.POST['url'])
    return HttpResponse(br.title(), mimetype="application/javascript")
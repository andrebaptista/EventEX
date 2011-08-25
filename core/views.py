#*-* coding: utf-8 *-*
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    home = True
    return render_to_response('index.html', {'home': home}, context_instance=RequestContext(request))
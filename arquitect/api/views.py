# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    vars = {}
    contexto = RequestContext(request)
    return render_to_response('homepage/index.html', vars, contexto)

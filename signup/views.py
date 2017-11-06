# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response
from django.template.context_processors import csrf


# Create your views here.
def signup_basic(request):
    form = UserCreationForm()
    #return render_to_response('index.html',{} ,form)
    #return render(request,'index.html',{form1:form1})
    token = {}
    token.update(csrf(request))
    token['form'] = form
    return render_to_response('index.html', token)

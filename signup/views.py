# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.contrib.auth import login, authenticate
from django.core.urlresolvers import reverse



# Create your views here.
def signup_basic(request):
    if(request.method == "POST"):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password)
            print user
            login(request,user)
            #return HttpResponseRedirect(reverse('home'))
            return redirect(reverse('home'))
    else:
        form = UserCreationForm()
    #return render_to_response('index.html',{'form':form})
    return render(request,'index.html',{'form':form})
    """
    token = {}
    token.update(csrf(request))
    token['form'] = form
    return render_to_response('index.html', token)
    """

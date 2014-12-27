#coding:utf-8
# Create your views here.
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from models import *
from forms import *
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from PIL import ImageFile

@login_required
def fitting(request):
    user = request.user
    try:
        profile = user.buyerprofile
    except:
        pass
    try:
        profile = user.sellerprofile
    except:
        pass
    if not profile:
        return HttpResponse('You are admin.')
    return render_to_response('fitting.html', RequestContext(request, {'profile': profile}),)


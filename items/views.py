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

@login_required
def addItem(request):
    """
    添加商品
    """
    if request.method == 'POST':
        user = request.user
        form = AddItemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            caption = form.cleaned_data['caption']
            newitem = Product(name=name,
                    caption = caption,
                    owner = user.sellerprofile
                    )
            newitem.save()
            return HttpResponseRedirect('/profile/%d' % user.id)
    return HttpResponseRedirect('/')

@login_required
def addMote(request):
    """
    添加模特
    """
    if request.method == 'POST':
        user = request.user
        form = AddMoteForm(request.POST, request.FILES)
        if form.is_valid():
            itemid = form.cleaned_data['item']
            try:
                item = Product.objects.get(id=itemid)
            except:
                return HttpResponse('Item does not exist.')
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            bust = form.cleaned_data['bust']
            waist = form.cleaned_data['waist']
            hip = form.cleaned_data['hip']
            arm_length = form.cleaned_data['arm_length']
            shoulder_width = form.cleaned_data['shoulder_width']
            leg_length = form.cleaned_data['leg_length']
            photo = form.cleaned_data['photo']
            newmote = Mote(
                    products = item,
                    height = height,
                    weight = weight,
                    bust = bust,
                    waist = waist,
                    hip = hip,
                    arm_length = arm_length,
                    shoulder_width = shoulder_width,
                    leg_length = leg_length,
                    photo = photo,
                    )
            newmote.save()
            return HttpResponseRedirect('/profile/%d' % user.id)
        else:
            print form.errors
            return HttpResponse('form error')
    return HttpResponseRedirect('/')

#coding:utf-8
# Create your views here.
from datetime import datetime
from django.http import HttpResponse
from models import *
from forms import *
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from PIL import ImageFile

@csrf_protect
def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            request.session['username'] = username
            request.session['password'] = password
            if request.POST.has_key('buyer'):
                return HttpResponseRedirect('/register1.html/register2/')
            else:
                return HttpResponseRedirect('/register1.html/register3/')
        else:
            variables = RequestContext(request, {'form':form})
            return render_to_response('register1.html', variables)
    else:
        form = RegistrationForm()
        variables = RequestContext(request, {'form':form})
        return render_to_response('register1.html', variables)

@csrf_protect
def register_page2(request):
    """
    先判断是否有session，若没有，则返回错误信息
    若有，则判断数据是否符合要求
    符合，则注册成功，保存资料到数据库，跳转到下一页
    """
    if "username" in request.session:
        if request.method == 'POST':
            form = RegistrationForm2(request.POST, request.FILES)
            if form.is_valid():
                height = form.cleaned_data['height']
                weight = form.cleaned_data['weight']
                bust = form.cleaned_data['bust']
                waist = form.cleaned_data['waist']
                hip = form.cleaned_data['hip']
                arm_length = form.cleaned_data['arm_length']
                shoulder_width = form.cleaned_data['shoulder_width']
                leg_length = form.cleaned_data['leg_length']
                introduction = form.cleaned_data['introduction']
                #对其图片进行操作
                sculpture = request.FILES.get('sculpture')
                # print sculpture
                #从缓存中取出用户名和密码
                username = request.session['username']
                password = request.session['password']
                
                #此处把数据传入数据库,创建
                user = User.objects.create_user(
                        username = username,
                        password = password
                        )
                newbuyer = BuyerProfile(buyer=user, height=height,
                        weight=weight, bust=bust, waist=waist, hip=hip,
                        arm_length=arm_length, shoulder_width=shoulder_width,
                        leg_length=leg_length, 
                        introduction=introduction
                        ) 
                if sculpture:
                    newbuyer.sculpture.save(str(datetime.now())+'.jpg', sculpture, save=False)
                newbuyer.save()

                #删除缓存
                del request.session['username']
                del request.session['password']
                return  HttpResponseRedirect('/register1.html/register_success')
            else:
                variables = RequestContext(request, {'form':form})
                return render_to_response('register2.html', variables)
        else:
            form = RegistrationForm2()
            variables = RequestContext(request, {'form':form})
            return render_to_response('register2.html', variables)

@csrf_protect
def register_page3(request):
    """
    同上
    """

def show_session(request):
    html = ""
    name = request.session["username"]
    password = request.session["password"]
    html = "get a session value: %s %s" % (str(name), str(password))
    del request.session['username']
    return HttpResponse(html)


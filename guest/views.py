#coding:utf-8
# Create your views here.
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from models import *
from forms import *
from items.forms import *
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import login, logout, authenticate
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
                return HttpResponseRedirect('/register/buyer')
            else:
                return HttpResponseRedirect('/register/seller')
        else:
            variables = RequestContext(request, {'form':form})
            return render_to_response('register1.html', variables)
    else:
        form = RegistrationForm()
        variables = RequestContext(request, {'form':form,})
        return render_to_response('register1.html', variables)

@csrf_protect
def register_page2(request):
    """
    先判断是否有session，若没有，则返回第一注册页
    若有，则判断数据是否符合要求
    符合，则注册成功，保存资料到数据库，跳转到成功页
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
                nickname = form.cleaned_data['nickname']
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
                        nickname=nickname,
                        introduction=introduction
                        ) 
                if sculpture:
                    newbuyer.sculpture.save(str(datetime.now())+'.jpg', sculpture, save=False)
                newbuyer.save()

                #删除缓存
                del request.session['username']
                del request.session['password']
                return  HttpResponseRedirect('/register/success')
            else:
                variables = RequestContext(request, {'form':form})
                return render_to_response('register2.html', variables)
        else:
            form = RegistrationForm2()
            variables = RequestContext(request, {'form':form})
            return render_to_response('register2.html', variables)
    else:
        return HttpResponseRedirect('/register')

@csrf_protect
def register_page3(request):
    """
    先判断是否有session，若没有，则返回第一注册页
    若有，则判断数据是否符合要求
    符合，则注册成功，保存资料到数据库，跳转到成功页
    """
    if "username" in request.session:
        if request.method == 'POST':
            form = RegistrationForm3(request.POST, request.FILES)
            if form.is_valid():
                nickname = form.cleaned_data['nickname']
                storename = form.cleaned_data['storename']
                email = form.cleaned_data['email']
                telephone = form.cleaned_data['telephone']
                company = form.cleaned_data['company']
                link = form.cleaned_data['link']
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
                newseller = SellerProfile(
                        seller=user,
                        nickname=nickname,
                        storename=storename,
                        telephone=telephone,
                        company=company,
                        link=link,
                        introduction=introduction
                        ) 
                if sculpture:
                    newseller.sculpture.save(str(datetime.now())+'.jpg', sculpture, save=False)
                newseller.save()

                #删除缓存
                del request.session['username']
                del request.session['password']
                return  HttpResponseRedirect('/register/success')
            else:
                variables = RequestContext(request, {'form':form})
                return render_to_response('register3.html', variables)
        else:
            form = RegistrationForm3()
            variables = RequestContext(request, {'form': form})
            return render_to_response('register3.html', variables)
    else:
        return HttpResponseRedirect('/register')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user) 
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('login failed.')
    return HttpResponseRedirect('/')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def home(request):
    return render_to_response('home.html', RequestContext(request))

@login_required
def resetPassword(request):
    """
    修改用户密码
    """
    if request.method == 'POST':
        user = request.user
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            newpassword = form.cleaned_data['newpassword1']
            user.set_password(newpassword)
            user.save()
    return HttpResponseRedirect('/')

@login_required
def modifyBuyerProfile(request):
    """
    修改买家资料
    """
    if request.method == 'POST':
        form = modify_buyer_profile_form(request.POST)
        if form.is_valid():
            user = request.user
            b = user.buyerprofile
            if form.cleaned_data['height']:
                b.height = form.cleaned_data['height']
            if form.cleaned_data['weight']:
                b.weight = form.cleaned_data['weight']
            if form.cleaned_data['bust']:
                b.bust = form.cleaned_data['bust'] 
            if form.cleaned_data['waist']:
                b.waist = form.cleaned_data['waist']
            if form.cleaned_data['hip']:
                b.hip = form.cleaned_data['hip']
            if form.cleaned_data['arm_length']:
                b.arm_length = form.cleaned_data['arm_length']
            if form.cleaned_data['shoulder_width']:
                b.shoulder_width = form.cleaned_data['shoulder_width']
            if form.cleaned_data['leg_length']:
                b.leg_length = form.cleaned_data['leg_length']
            if form.cleaned_data['nickname']:
                b.nickname = form.cleaned_data['nickname']
            if form.cleaned_data['sculpture']:
                b.sculpture = form.cleaned_data['sculpture']
            if form.cleaned_data['introduction']:
                b.introduction = form.cleaned_data['introduction']
            b.save()
            return HttpResponseRedirect('/profile/%d' % user.id)
    return HttpResponseRedirect('/')            
   
@login_required
def modifySellerProfile(request):
    """
    修改卖家资料
    """
    if request.method == 'POST':
        form = modify_seller_profile_form(request.POST)
        if form.is_valid():
            user = request.user
            s = user.sellerprofile
            if form.cleaned_data['nickname']:
                s.nickname = form.cleaned_data['nickname']
            if form.cleaned_data['storename']:
                s.storename = form.cleaned_data['storename'] 
            if form.cleaned_data['email']:
                user.email = form.cleaned_data['email']
            if form.cleaned_data['telephone']:
                s.telephone = form.cleaned_data['telephone']
            if form.cleaned_data['company']:
                s.company = form.cleaned_data['company']
            if form.cleaned_data['link']:
                s.link = form.cleaned_data['link']
            if form.cleaned_data['sculpture']:
                s.sculpture = form.cleaned_data['sculpture']
            if form.cleaned_data['introduction']:
                s.introduction = form.cleaned_data['introduction']
            s.save()
            return HttpResponseRedirect('/profile/%d' % user.id)
    return HttpResponseRedirect('/')

@login_required
def profile(request, userid):
    """
    获取用户主页
    判断用户id是卖家还是买家
    如果是卖家则返回一个卖家主页seller_page.html
    如果是买家则返回一个买家主页buyer_page.html
    """
    usertmp = request.user
    if(usertmp.id == 1):
        return HttpResponse("管理员账户")
    if(usertmp.id != int(userid)):
        return HttpResponse("errors, you can't access other's page")

    resetpassword_form = ResetPasswordForm()
    try:
        profile = usertmp.buyerprofile
        modify_buyer_profile_form = ModifyBuyerProfileForm(
                initial={
                    'height': profile.height,
                    'weight': profile.weight,
                    'bust': profile.bust,
                    'waist': profile.waist,
                    'hip': profile.hip,
                    'arm_length': profile.arm_length,
                    'shoulder_width': profile.shoulder_width,
                    'leg_length': profile.leg_length,
                    'nickname': profile.nickname,
                    'introduction': profile.introduction,
                    }
                )
        return render_to_response(
                'buyer_page.html', 
                RequestContext(
                    request, 
                    {
                        'modify_buyer_profile_form': modify_buyer_profile_form,
                        'resetpassword_form': resetpassword_form,
                        'profile': profile,
                    }))
    except:
        pass
    try:
        profile = usertmp.sellerprofile
        modify_seller_profile_form = ModifySellerProfileForm(
                initial={
                    'nickname': profile.nickname,
                    'storename': profile.storename,
                    'email': usertmp.email,
                    'telephone': profile.telephone,
                    'company': profile.company,
                    'link': profile.link,
                    'introduction': profile.introduction,
                    }
                )
        add_item_form = AddItemForm()
        return render_to_response(
                'seller_page.html', 
                RequestContext(
                    request, 
                    {
                        'modify_seller_profile_form': modify_seller_profile_form,
                        'resetpassword_form': resetpassword_form,
                        'profile': profile,
                        'add_item_form':AddItemForm,
                    }))
    except:
        pass
    return HttpResponse('未知错误')

def _show_session(request):
    html = ""
    name = request.session["username"]
    password = request.session["password"]
    html = "get a session value: %s %s" % (str(name), str(password))
    del request.session['username']
    return HttpResponse(html)


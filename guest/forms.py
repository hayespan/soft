#coding:utf-8
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

class RegistrationForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=30)
    password1 = forms.CharField(label='密码', widget=forms.PasswordInput())
    password2 = forms.CharField(label='确认密码', widget=forms.PasswordInput())
    
    def clean_username(self):
        '''
        验证用户名的合法性
        '''
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('用户名中只能包含字母、数字和下划线！')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('用户名已存在！')
        
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
            raise forms.ValidationError('两次密码不一致')

class RegistrationForm2(forms.Form):
    height = forms.IntegerField(label='身高(cm)')
    weight = forms.IntegerField(label='体重(kg)')
    bust = forms.IntegerField(label='胸围(cm)')
    waist = forms.IntegerField(label='腰围(cm)')
    hip = forms.IntegerField(label='臀围(cm)')
    arm_length = forms.IntegerField(label='手长(cm)')
    shoulder_width = forms.IntegerField(label='肩宽(cm)')
    leg_length = forms.IntegerField(label='腿长(cm)')
    nickname = forms.CharField(label='个人昵称')
    sculpture = forms.ImageField(label='个人头像', required=False)
    introduction = forms.CharField(label='个人简介', widget=forms.Textarea(attrs={'size':10000}), required=False)

class RegistrationForm3(forms.Form):
    nickname = forms.CharField(label='昵称', max_length=20)
    storename = forms.CharField(label='店名', max_length=30)
    email = forms.EmailField(label='邮箱')
    telephone = forms.CharField(label='电话', max_length=11)
    company = forms.CharField(label='公司', max_length=100)
    link = forms.URLField(label='链接')
    sculpture = forms.ImageField(label='头像')
    introduction = forms.CharField(label='简介', widget=forms.Textarea(attrs={'size':10000}), required=False)

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密码')

class ResetPasswordForm(forms.Form):
    oldpassword = forms.CharField(label='旧密码')
    newpassword1 = forms.CharField(label='新密码')
    newpassword2 = forms.CharField(label='确认新密码')
    def clean_newpassword1(self):
        if self.cleaned_data['newpassword1'] == self.cleaned_data['oldpassword']:
            raise ValidationError('新旧密码相同')
        return self.cleaned_data['newpassword1']
    def clean_newpassword2(self):
        if self.cleaned_data['newpassword1'] != self.cleaned_data['newpassword2']:
            raise ValidationError('密码不一致')
        return self.cleaned_data['newpassword2']

class ModifyBuyerProfileForm(forms.Form):
    height = forms.IntegerField(label='身高(cm)', required=False)
    weight = forms.IntegerField(label='体重(kg)', required=False)
    bust = forms.IntegerField(label='胸围(cm)', required=False)
    waist = forms.IntegerField(label='腰围(cm)', required=False)
    hip = forms.IntegerField(label='臀围(cm)', required=False)
    arm_length = forms.IntegerField(label='手长(cm)', required=False)
    shoulder_width = forms.IntegerField(label='肩宽(cm)', required=False)
    leg_length = forms.IntegerField(label='腿长(cm)', required=False)
    nickname = forms.CharField(label='个人昵称', required=False)
    sculpture = forms.ImageField(label='个人头像', required=False)
    introduction = forms.CharField(label='个人简介', widget=forms.Textarea(attrs={'size':10000}), required=False)

class ModifySellerProfileForm(forms.Form):
    nickname = forms.CharField(label='昵称', max_length=20, required=False)
    storename = forms.CharField(label='店名', max_length=30, required=False)
    email = forms.EmailField(label='邮箱', required=False)
    telephone = forms.CharField(label='电话', max_length=11, required=False)
    company = forms.CharField(label='公司', max_length=100, required=False)
    link = forms.URLField(label='链接', required=False)
    sculpture = forms.ImageField(label='头像', required=False)
    introduction = forms.CharField(label='简介', required=False)


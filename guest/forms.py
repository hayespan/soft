#coding:utf-8
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
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
    height = forms.IntegerField(label='身高(cm)',
            widget=forms.TextInput(attrs={'size':3,}))
    weight = forms.IntegerField(label='体重(kg)',
        widget=forms.TextInput(attrs={'size':3,}))
    bust = forms.IntegerField(label='胸围(cm)',
            widget=forms.TextInput(attrs={'size':3,}))
    waist = forms.IntegerField(label='腰围(cm)',
            widget=forms.TextInput(attrs={'size':3,}))
    hip = forms.IntegerField(label='臀围(cm)',
            widget=forms.TextInput(attrs={'size':3,}))
    arm_length = forms.IntegerField(label='手长(cm)',
            widget=forms.TextInput(attrs={'size':3,}))
    shoulder_width = forms.IntegerField(label='肩宽(cm)',
            widget=forms.TextInput(attrs={'size':3,}))
    leg_length = forms.IntegerField(label='腿长(cm)',
            widget=forms.TextInput(attrs={'size':3,}))
    sculpture = forms.ImageField(label='头像', required=False)
    introduction = forms.CharField(label='简介',
            widget=forms.Textarea(attrs={'size':10000}), required=False)

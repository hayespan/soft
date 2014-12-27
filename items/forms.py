#coding:utf-8
from django import forms

class AddItemForm(forms.Form):
    name = forms.CharField(label='商品名称', max_length=30)
    caption = forms.CharField(label='商品描述')

class AddMoteForm(forms.Form):
    height = forms.IntegerField(label='身高')
    weight = forms.IntegerField(label='体重')
    bust = forms.IntegerField(label='胸围')
    waist = forms.IntegerField(label='腰围')
    hip = forms.IntegerField(label='臀围')
    arm_length = forms.IntegerField(label='手长')
    shoulder_width = forms.IntegerField(label='肩宽')
    leg_length = forms.IntegerField(label='腿长')
    photo = forms.IntegerField(label='模特照片')

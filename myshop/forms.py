from django import forms
from django.forms import ModelForm
from myshop import models

class LoginForm(forms.Form):
    username = forms.CharField(label='帳號', max_length=10)
    password = forms.CharField(label='密碼', widget=forms.PasswordInput())

class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ['full_name', 'address', 'phone']
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].label = '收件人姓名'
        self.fields['address'].label = '郵寄地址'
        self.fields['phone'].label = '聯絡電話'

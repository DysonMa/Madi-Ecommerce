from django import forms
from django.forms import ModelForm
from myshop import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['male']

    def __init__(self):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['male'].label = '是男生嗎'

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="密碼確認",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
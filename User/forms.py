from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.forms import Form
from django.forms import fields
from django import forms

from User.models import User


class RegisterForm(forms.Form):
    email = fields.EmailField()
    username = fields.CharField()
    password = fields.CharField()
    avatar = fields.FileField(required=False)


class LoginForm(forms.Form):
    username = fields.CharField()
    password = fields.CharField()
    next = fields.CharField(required=False)


# 信息修改表單
class ChangeInfoForm(forms.Form):
    username = fields.CharField()
    password = fields.CharField()
    avatar = fields.FileField(required=False)


class Modify_Input_Form(forms.Form):
    email = fields.EmailField()
    password = fields.CharField()


class BindEmail(forms.Form):
    avatar = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'avatar'}), required=False)
    type = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'type'}))
    openid = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'openid'}))
    username = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'username'}))
    email = forms.EmailField(label=u'绑定邮箱', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'id': 'email', 'placeholder': u'请输入用于绑定本站账号的邮箱',
               'oninvalid': "setCustomValidity('请输入正确的邮箱地址');", 'oninput': "setCustomValidity('');"}))
    password = forms.CharField(label=u'用户密码', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'password', 'placeholder': u'若尚未注册过本站账号，则该密码作为账户密码',
               "oninvalid": "setCustomValidity('请输入绑定用户的密码');", 'oninput': "setCustomValidity('');"}))

    def clean_email(self):  # 查询邮箱是否已经被绑定
        email = self.cleaned_data.get('email')
        type = self.cleaned_data.get('type')
        users = User.objects.filter(email=email)
        if users:
            if OAuth_ex.objects.filter(user=users[0], type=type):
                raise ValidationError(u'邮箱已经被绑定了')
        return email

    def clean_password(self):  # 验证密码是否输入正确
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        users = User.objects.filter(email=email)
        if users:
            user = authenticate(email=email, password=password)
            if user:
                return password
            else:
                raise ValidationError(u'密码不正确，绑定失败')
        return password

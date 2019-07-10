import time

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response

# Create your views here.
from django.urls import reverse
from django.views.generic.base import View

from NewDjango.settings import GIT_ClIENT_ID, GIT_ClIENT_SECRET, GIT_CALLBACK_URL
from Oauth.BASE_OAUTH import OAuth_github
from User.forms import RegisterForm, LoginForm, Modify_Input_Form, ChangeInfoForm, BindEmail
from User.models import User, OAuth_ex


class Register(View):
    def get(self, request):
        return render(request, 'user/register.html')

    def post(self, request):
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            avatar = form.cleaned_data['avatar']
            email = form.cleaned_data['email']

            user = User()
            user.username = username
            user.set_password(password)
            user.email = email
            user.avatar = avatar
            user.save()

            return redirect(reverse('User:login'))
        else:
            return render(request, 'user/register.html', {'msg': '請爭取輸入！'})


class Login(View):
    def get(self, request):
        next = request.GET.get('next','')
        print('next',next)
        return render(request, 'user/login.html', {'next': next})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            next = form.cleaned_data['next']

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                request.session['is_login'] = True
                request.session['user_name'] = username
                if next:
                    return HttpResponseRedirect(next)
                return redirect(reverse('Index:index'))
        return render(request, 'user/login.html', {'msg': '请正确录入！'})


class Quit(View):
    def get(self, request):
        logout(request)
        request.session.flush()
        return redirect(reverse('Index:index'))


class RegisterCheck(View):
    def post(self, request):
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        if username:
            user = User.objects.filter(username=username)
            if user:
                return JsonResponse({'name': 'fail'})
            else:
                return JsonResponse({'name': 'ok'})

        if email:
            user = User.objects.filter(email=email)
            if user:
                return JsonResponse({'email': 'fail'})
            else:
                return JsonResponse({'email': 'ok'})


class Modify(View):
    def get(self, request):
        return render(request, 'user/modify.html')

    def post(self, request):
        form = Modify_Input_Form(request.POST)
        if form.is_valid():
            return render(request, 'user/chinfo.html')
        else:
            return render(request, 'user/modify.html', {'msg': '请正确输入！'})


class ModifyCheck(View):
    def post(self, request):
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        username = request.user.username
        uid = request.user.id
        user = User.objects.get(pk=uid)
        if email:
            if user.email == email:
                return JsonResponse({'email': 'ok'})
            else:
                return JsonResponse({'email': 'fail'})

        if password:
            user = authenticate(username=username, password=password)
            if user:
                return JsonResponse({'password': 'ok'})
            return JsonResponse({'password': 'fall'})


class ChangeInfo(View):
    def post(self, request):
        form = ChangeInfoForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            avatar = form.cleaned_data['avatar']

            uid = request.user.id
            user = User.objects.get(pk=uid)
            user.username = username
            user.set_password(password)
            user.avatar = avatar
            user.save()
            return redirect(reverse('Index:index'))
        return render(request, 'user/chinfo.html', {'msg': '請正確輸入！'})


# git
def github_login(request):
    oauth_git = OAuth_github(GIT_ClIENT_ID, GIT_ClIENT_SECRET, GIT_CALLBACK_URL)
    url = oauth_git.get_auth_url()
    print(url)
    return HttpResponseRedirect(url)


def github_check(request):
    type = '1'
    request_code = request.GET.get('code')
    oauth_git = OAuth_github(GIT_ClIENT_ID, GIT_ClIENT_SECRET, GIT_CALLBACK_URL)
    try:
        access_token = oauth_git.get_access_token(request_code)
        time.sleep(0.1)
    except:
        data = {}
        data['goto_url'] = '/'
        data['goto_time'] = 10000
        data['goto_page'] = True
        data['message_title'] = '登录失败'
        data['message'] = '获取授权失败，请确认是否允许授权，并重试。若问题无法解决，请联系网站管理人员'
        return render_to_response('oauth/response.html', data)

    user_info = oauth_git.get_user_info()
    username = user_info.get('login', '')
    avatar = user_info.get('avatar_url', '')
    openid = str(oauth_git.openid)
    print(username, avatar, openid)

    # 查询是否绑定
    github = OAuth_ex.objects.filter(openid=openid, type=type)
    if github:
        login(request, github[0].user)
        return redirect(reverse('index'))
    else:
        try:
            email = oauth_git.get_email()
        except:
            url = "%s?username=%s&openid=%s&type=%s&avatar=%s" % (
                redirect(reverse('user:bind_email')), username, openid, type, avatar)
            return HttpResponseRedirect(url)

    users = User.objects.filter(email=email)
    if users:
        user = users[0]
    else:
        while User.objects.filter(username=username):  # 防止用户名重复
            username = username + '*'
        user = User(username=username, email=email)
        pwd = '123456'  # 随机设置用户密码
        user.set_password(pwd)
        user.is_active = True
        user.avatar = avatar  # 下载用户头像图片
        user.oauth = 1
        user.save()

    oauth_ex = OAuth_ex(user=user, openid=openid, type=type)
    oauth_ex.save()
    login(request, user)
    data = {}  # 反馈登陆结果
    data['goto_url'] = '/'
    data['goto_time'] = 10000
    data['goto_page'] = True
    data['message_title'] = '绑定用户成功'
    data['message'] = u'绑定成功！您的用户名为：<b>%s</b>。您现在可以同时使用本站账号和此第三方账号登录本站了！' \
                      u'初始密码 123456 ！' \
                      u'请尽快更改！' % username
    return render_to_response('oauth/response.html', data)


def bind_email(request):
    openid = request.GET.get('openid', request.POST.get('openid', ''))
    username = request.GET.get('nickname', request.POST.get('username', ''))
    type = request.GET.get('type', request.POST.get('type', ''))
    avatar = request.GET.get('avatar', request.POST.get('avatar', ''))

    if request.method == 'POST':
        form = BindEmail(request.POST)
        if form.is_valid():
            openid = form.cleaned_data['openid']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            type = form.cleaned_data['type']
            avatar = form.cleaned_data['avatar']
            users = User.objects.filter(email=email)
            if users:
                user = users[0]
            else:
                while User.objects.filter(username=username):
                    username = username + '*'
                user = User(username=username, email=email)
                user.set_password(password)
                user.is_active = True
                user.avatar = avatar
                user.oauth = True
                user.save()
            oauth_ex = OAuth_ex(user=user, openid=openid, type=type)
            oauth_ex.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            data = {}
            data['goto_url'] = '3397/'
            data['goto_time'] = 10000
            data['goto_page'] = True
            data['message_title'] = '绑定账号成功'
            data['message'] = u'绑定成功！您的用户名为：<b>%s</b>。您现在可以同时使用本站账号和此第三方账号登录本站了！' % username
            return render_to_response('oauth/response.html', data)

    else:
        form = BindEmail(initial={
            'openid': openid,
            'nickname': username,
            'type': type,
            'image_url': avatar,

        })
        return render(request, 'oauth/bind_email.html', context={'form': form, 'type': type})

from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from myshop import models, forms
from django.contrib import messages
from django.contrib.sessions.models import Session

# auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required 

# Create your views here.
@login_required(login_url='/login')
def index(request):
    if request.user.is_authenticated:
        username = request.user.username
    all_products = models.Product.objects.all()

    paginator = Paginator(all_products, 4)  # 一頁顯示4個
    p = request.GET.get('p')                # 讀取網址中的?p=...的數字當作參數
    try:
        products = paginator.page(p)        # 取得指定頁數，回傳一個page物件
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    # template = get_template('index.html')
    # request_context = request_context

    return render(request, 'index.html', locals())

def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)  # POST 初始化LoginForm
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            try:
                user = authenticate(username=login_name, password=login_password)  # auth驗證，若失敗，user為None
                if user is not None:
                    if user.is_active:             # 檢查此帳號是否有效
                        auth.login(request, user)  # 把此使用者的資料存入session，供其他網頁使用
                    messages.add_message(request, messages.SUCCESS, '登入成功')
                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING, '登入失敗')
            except:
                messages.add_message(request, messages.WARNING, '找不到該使用者')
        else:
            messages.add_message(request, messages.INFO, '請檢查輸入的欄位')
    else:
        login_form = forms.LoginForm()  # GET 初始化LoginForm

    return render(request, 'login.html', locals())

def logout(request):
    auth.logout(request) # auth登出
    messages.add_message(request, messages.INFO, '成功登出')
    return redirect('/')

@login_required(login_url='/login/')  # userinfo 必須登入後才能執行，否則導向/login
def userinfo(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        return redirect('/login')
    try:
        userinfo = User.objects.get(username=username)
    except:
        pass

    return render(request, 'userinfo.html', locals()) 
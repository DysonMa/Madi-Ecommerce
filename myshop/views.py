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
from allauth.account.decorators import verified_email_required

# SMTP
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# cart
from cart.cart import Cart

# Create your views here.
@login_required(login_url='/login')
def index(request, cat_id=0):
    if request.user.is_authenticated:
        username = request.user.username
    
    # 處理category的id
    if cat_id >= 0:
        try:
            category = models.Category.objects.get(id=cat_id)
            all_products = models.Product.objects.filter(category=category)
        except:
            category = None
            all_products = models.Product.objects.all()

    all_categories = models.Category.objects.all()
    paginator = Paginator(all_products, 4)  # 一頁顯示4個
    p = request.GET.get('p')                # 讀取網址中的?p=...的數字當作參數
    try:
        products = paginator.page(p)        # 取得指定頁數，回傳一個page物件
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
    # 自己計算cart總數量
    cart = Cart(request)
    dic = list(cart.session['cart'].values())
    cnt = sum([each['quantity'] for each in dic]) 
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
        user = User.objects.get(username=username)
        userinfo = models.Profile.objects.get(user=user)
    except:
        pass

    all_categories = models.Category.objects.all()

    return render(request, 'userinfo.html', locals()) 


@login_required(login_url='/login/')
def product(request, product_id):
    if request.user.is_authenticated:
        username = request.user.username
    all_categories = models.Category.objects.all()
    try:
        product = models.Product.objects.get(id=product_id)
    except:
        product = None
    
    return render(request, 'product.html', locals())

def add_to_cart(request, product_id, quantity):
    product = models.Product.objects.get(id=product_id)
    cart = Cart(request)  # django的cart套件
    cart.add(product, product.price, quantity)
    return redirect('/')

def remove_from_cart(request, product_id):
    product = models.Product.objects.get(id=product_id)
    cart = Cart(request)  # django的cart套件
    cart.remove(product)
    return redirect('/cart/')

@login_required(login_url='/login/')
def cart(request):
    if request.user.is_authenticated:
        username = request.user.username
    all_categories = models.Category.objects.all()
    
    # 自己計算總額
    cart = Cart(request)
    dic = list(cart.session['cart'].values())
    total_price = sum([each['quantity']*(float(each['price'])) for each in dic])

    return render(request, 'cart.html', locals())

# @verified_email_required
def order(request):
    if request.user.is_authenticated:
        username = request.user.username
    all_categories = models.Category.objects.all()
    
    # 自己計算總額
    cart = Cart(request)
    dic = list(cart.session['cart'].values())
    total_price = sum([each['quantity']*(float(each['price'])) for each in dic])
    
    if request.method=='POST':
        user = User.objects.get(username=request.user.username)
        new_order = models.Order(user=user)
        form = forms.OrderForm(request.POST, instance=new_order)
        if form.is_valid():
            order = form.save()  # 把訂單Order儲存在資料庫中並取得實例放在order這個變數中
            print(request)
            email_messages = '購物內容如下: \n'
            for prod in cart.session['cart'].values():
                models.OrderItem.objects.create(order=order,
                                                # product=prod['name'],  # Heroku無法修改cart.py的model，所以暫時不join到product
                                                name=prod['name'],
                                                price=prod['price'],
                                                quantity=prod['quantity'])
                email_messages = f'{email_messages}\n{prod["name"]}, 價格: {float(prod["price"])}, 數量: {prod["quantity"]}個'
            cart.clear()  # 清除購物車內容

            # 電子郵件內容樣板
            email_template = render_to_string(
                'order_success_email.html',
                {'email_messages': email_messages}
            )
            email_seller = EmailMessage(
                '訂購產品通知',  # 電子郵件標題
                email_template,  # 電子郵件內容
                settings.EMAIL_HOST_USER,  # 寄件者
                ['madihsiang@gmail.com']  # 收件者
            )
            email_customer = EmailMessage(
                '感謝您的訂購',  # 電子郵件標題
                email_template,  # 電子郵件內容
                settings.EMAIL_HOST_USER,  # 寄件者
                [request.user.email]  # 收件者
            )
            email_seller.fail_silently = False
            email_customer.fail_silently = False
            email_seller.send()
            email_customer.send()

            return redirect('/myorders/')
    else:
        form = forms.OrderForm()

    return render(request, 'order.html', locals())

@login_required(login_url='/login/')
def my_orders(request):
    if request.user.is_authenticated:
        username = request.user.username
    all_categories = models.Category.objects.all()
    orders = models.Order.objects.filter(user=request.user)

    return render(request, 'myorders.html', locals())

# 註冊
def sign_up(request):
    form = forms.RegisterForm()
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # 電子郵件內容樣板
            email_template = render_to_string(
                'registration/signup_success_email.html',
                {'username': request.user.username}
            )
            email = EmailMessage(
                'Madi-Ecommerce註冊成功通知信',  # 電子郵件標題
                email_template,  # 電子郵件內容
                settings.EMAIL_HOST_USER,  # 寄件者
                ['madihsiang@gmail.com']  # 收件者
            )
            email.fail_silently = False
            email.send()
            return redirect('/login')
    context = {
        'form': form
    }
    return render(request, 'registration/registration_form.html', context)
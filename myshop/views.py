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

    cart = Cart(request) # 購物車
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


@login_required(login_url='/login/')
def product(request, product_id):
    if request.user.is_authenticated:
        username = request.user.username
    all_categories = models.Category.objects.all()
    try:
        product = models.Product.objects.get(id=product_id)
    except:
        product = None
    
    # template = get_template('product.html')
    # request_context = 
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
    cart = Cart(request) # django的cart套件
    return render(request, 'cart.html', locals())

# @verified_email_required
def order(request):
    all_categories = models.Category.objects.all()
    cart = Cart(request)
    if request.method=='POST':
        user = User.objects.get(username=request.user.username)
        new_order = models.Order(user=user)

        form = forms.OrderForm(request.POST, instance=new_order)
        if form.is_valid():
            order = form.save()  # 把訂單Order儲存在資料庫中並取得實例放在order這個變數中
            email_messages = '您的購物內容如下: \n'
            for item in cart:
                models.OrderItem.objects.create(order=order,
                                                product=item.product,
                                                price=item.product.price,
                                                quantity=item.quantity)
            email_messages = f'{email_messages}\n{item.product}, {item.product.price}, {item.quantity}'
            cart.clear()  # 清除購物車內容
            messages.add_message(request, messages.INFO, '訂單已儲存，我們會盡快處理。')
            # 訂購者
            send_mail('感謝您的訂購',
                        email_messages,
                        '迷你電商',
                        [request.user.email],)
            # 管理員
            send_mail('有人訂購產品囉',
                        email_messages,
                        '迷你電商',
                        ['madihsiang@gmail.com'],)
            return redirect('/myorders/')
    else:
        form = forms.OrderForm()

    return render(request, 'order.html', locals())

@login_required(login_url='/login/')
def my_orders(request):
    all_categories = models.Category.objects.all()
    orders = models.Order.objects.filter(user=request.user)

    return render(request, 'myorders.html', locals())


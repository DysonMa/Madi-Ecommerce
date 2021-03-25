# Madi-Ecommerce

* 這是一個用 Django, Bootstrap, MySQL(或SQLite), Docker 架設並部署在 Heroku 的購物網站。

![home](/static/githubImages/4.PNG)

## 功能
* 響應式(RWD)網站設計
* 首頁圖片輪播(Carousel)
* 首頁商品導覽換頁(Paginator)
* 使用者登入驗證與註冊(django auth)
* 第三方登入驗證(Google、GitHub)
* 利用URL patterns增刪購物車內容(Restful API)
* 將商品加入購物車(django-shopping-cart)並提交訂單(session)
* 發送訂單確認的電子郵件給顧客(SMTP + Gmail)
* Admin管理後臺可以上傳產品圖片(django-filer)

## 使用技術與工具
* 前端:
    - HTML5
    - CSS3
    - jquery
    - [Bootstrap(4.5.2)](https://getbootstrap.com/)
* 後端:
    - [Django(3.1.7)](https://www.djangoproject.com/)
        - session
        - form
        - email(SMTP+Gmail)
        - django-allauth(Google、GitHub)  
        - django-shopping-cart
        - djagno-filer
* 資料庫:
    - [MySQL](https://www.mysql.com/)
    - [PostgreSQL(Heroku)](https://www.postgresql.org/)
    - [SQLite](https://www.sqlite.org/index.html)
* 部署:
    - [Docker](https://www.docker.com/)
    - [Heroku](https://dashboard.heroku.com/)

## 演示步驟與展示圖片

* 尚未有帳號密碼，所以導至登入頁面
<img src='/static/githubImages/14.PNG' width='750px'>

* 第三方登入(Google、GitHub)
<img src='/static/githubImages/15.PNG' width='500px'>
<img src='/static/githubImages/16.PNG' width='500px'>

* 或是註冊帳號，成功後會寄發註冊成功的電子郵件
<img src='/static/githubImages/17.PNG' width='750px'>
<img src='/static/githubImages/18.PNG' width='750px'>

* 登入成功後，進入首頁
<img src='/static/githubImages/4.PNG' width='750px'>

* 使用者個人資料
<img src='/static/githubImages/7.PNG' width='750px'>

* 分類檢視，例如選擇"書籍"
<img src='/static/githubImages/5.PNG' width='750px'>
<img src='/static/githubImages/6.PNG' width='750px'>

* 選購商品，加入購物車
<img src='/static/githubImages/8.PNG' width='750px'>
<img src='/static/githubImages/9.PNG' width='750px'>
<img src='/static/githubImages/10.PNG' width='750px'>

* 按下"我要訂購"，並輸入訂購資訊，再按下"下訂單"
<img src='/static/githubImages/11.PNG' width='750px'>
<img src='/static/githubImages/12.PNG' width='750px'>

* 發送電子郵件通知訂單給顧客
<img src='/static/githubImages/13.PNG' width='750px'>

* 若想增加商品圖片，可以在Admin管理後臺上傳圖片
<img src='/static/githubImages/1.PNG' width='750px'>
<img src='/static/githubImages/2.PNG' width='750px'>

## 資料表設計與正規化
底下為MySQL Workbench的EER Diagram

<img src='/static/githubImages/21.PNG' width='750px'>

* `myshop_product`: 是 **商品** 的資料表，有 `sku`, `name`, `description`, `stock`, `price`...等欄位

* `myshop_category`: 是 **商品類別** 的資料表，有 `name` 這個欄位，並以 `category_id` 為 Foreign key 與 `myshop_product` 資料表做關聯

* `auth_user`: **是 Django auth 內建的 user(使用者) model**，有內建的欄位，ex: `password`, `last_login`, `username`...

* `myshop_profile`: **擴充內建的 user(使用者) model**，多增加一個 `male`的欄位，並以 `user_id` 為 foreign key 與 `auth_user` 資料表做關聯

* `myshop_order`: 按下 **"我要訂購"** 所儲存的資料表，內含訂購填寫的 `full_name`, `address`, `phone`...等欄位，並以 `user_id` 為 foreign key 與 `auth_user` 資料表做關聯

* `myshop_orderitem`: 按下 **"下訂單"** 所儲存的資料表，內含訂單詳細資訊如 `price`, `quantity`, `name`...等欄位，並以 `order_id` 為 foreign key 與 `myshop_order` 資料表做關聯

* `cart_item`: **是 Django-shopping-cart 內建的購物車內容** 的資料表，有 `quantity`, `unit_price`...等欄位


## 本地端建立環境
### 安裝
遠端下載repo
```
git clone https://github.com/DysonMa/Madi-Ecommerce.git
```

### 編輯config.ini
以下是範本，要依照個人需求修改
```
[Django]
SECRET_KEY = 

[Gmail]
email = 
client_secret = 

[MySQL]
client_secret = 
```

* `[Django] SECRET_KEY`: 可以不用編輯，因為是demo版，所以仍然附在code裡面
* `[Gmail] email`: 輸入寄件者的信箱
* `[Gmail] client_secret`: 用來核准寄信的密鑰，須至 [Google Gmail API 申請](https://developers.google.com/gmail/api/quickstart/js) 申請，詳細步驟可以參考[這裡](https://www.learncodewithmike.com/2020/04/django-allauth-google.html)
* `[MySQL] client_secret`: 用來連線MySQL的密碼 

### 手動啟動
1. 進入資料夾
```
cd Madi-Ecommerce
```
2. 創建一個虛擬環境叫做 `myenv`
```
python -m venv myvenv
```
3. 開啟虛擬環境
```
myvenv\Scripts\activate
```
4. pip安裝相依的套件
```
pip install -r requirements.txt
```
5. migrate資料
```
python manage.py makemigrations
python manage.py migrate
```
6. 建立superuser，輸入使用者名稱/Password
```
python manage.py createsuperuser
```
7. 在本地端 run server
```
python manage.py runserver
```
8. 到 https://localhost:8000/ 就可以看到網站
9. 利用剛剛輸入的使用者名稱/Password登入網站

### 利用Docker啟動
1. 進入資料夾
```
cd Madi-Ecommerce
```
2. 利用 `docker-compose` 建立並啟動環境
```
docker-compose up --build
docker-compose up
```
3. 查看 container 的 ID
```
docker ps -a
```
4. 進入bash
```
docker exec -it <Web Container ID> bash
```
5. 在 bash 輸入指令，migrate資料
```
python manage.py makemigrations
python manage.py migrate
```
3. 在 bash 輸入指令，建立superuser，輸入使用者名稱/Password
```
python manage.py createsuperuser
```
4. 到 https://localhost:8000/ 就可以看到網站
5. 利用剛剛輸入的使用者名稱/Password登入網站

### 手動增加商品
1. 因為資料庫是全新的，所以商品需要手動加入
2. 點選上方導覽列的 `後臺管理`，再點選左邊 `MYSHOP/Categorys`，點選右上方的 `新增 CATEGORY`，輸入想增加的商品類別
3. 點選左邊 `MYSHOP/Products`，點選右上方的 `新增 PRODUCT`，會看到下圖即可開始依照欄位建立商品，圖片可以從 `static/images`裏頭上傳

<img src='/static/githubImages/19.PNG' width='750px'>

### 第三方登入驗證申請步驟
1. 需要到 [Google-API-Dashboard](https://console.cloud.google.com/apis/dashboard) 申請一組憑證，並記錄下來
2. 需要到 [Github 第三方驗證](https://github.com/settings/applications/new)上方申請一組憑證，並記錄下來
3. 點選上方導覽列的 `後臺管理`，再點選左邊 `網站/網站`，點選中間的 `example.com`，網域名稱改為 `localhost:8000/`，顯示名稱改為 `localhost`
4. 再點選左邊 `社群帳號/社群應用程式`，點選右上方的 `新增 社群應用程式`，進到下面畫面，選擇Google或GitHub，並輸入剛剛申請的憑證，接著別忘了底下的 `localhost:8000/` 要加入到右邊，底下是Google的範例。 

<img src='/static/githubImages/20.PNG' width='750px'>

詳細教學:

* [Google 第三方驗證-教學](https://www.learncodewithmike.com/2020/04/django-allauth-google.html)
* [Google Gmail API 申請](https://developers.google.com/gmail/api/quickstart/js)
* [Google-API-Dashboard](https://console.cloud.google.com/apis/dashboard)
* [Github 第三方驗證-教學](https://ithelp.ithome.com.tw/articles/10241844)

### Heroku部署步驟
* [Heroku 部署(1)](https://djangogirlstaipei.herokuapp.com/tutorials/deploy-to-heroku/?os=windows)
* [Heroku 部署(2)](https://ithelp.ithome.com.tw/articles/10212659?sc=rss.qu)

## 專案上遇到的問題
### Config組態設定
* 因為部署到 github 會有 `client_secret` 外露的資安問題，所以編輯一個 `config.ini` 的組態設定檔，內含各種密碼，透過 `configer` 的讀取方式，避免暴露密碼，也方便統一管理所需要的參數

### Django套件
* `django-shopping-cart` 內建的 `add` 函式無法存取 product，導致 `OrderItem` 這個 model 無法跟 `Product` 這個 model 以 foreign key 做關聯，地端程式碼可以手動修改，但部署到 Heroku 就無法修改套件py檔內容，因此最後 Heroku app 取消關聯到 `Product` 這個資料表
* `python manage.py makemigrations` 若失效，要進到 `migrations` 資料夾，手動查找每個版本的py檔，找出與model修正有關聯的檔案，手動修正或刪除，重新執行此指令即可成功運行

### Heroku部署
* 本機作業環境是 Windows，利用 `pip freeze > requirements.txt` 指令會生成 `pywin300`這個套件，但Heroku是Linux環境，所以會部署失敗，需要手動刪除此套件
* Heroku 預設的資料庫是 PostgreSQL，因此 `settings` 裏頭要修改DB連結的方式，才能在 Heroku 上部署成功
* Heroku 部署需要提供三個檔案，`Procfile`、`requirements.txt`、`runtime.txt`

## Backend學習筆記與部落格
### [My HackMD](https://hackmd.io/@MaDi)
* [Docker基本概念與操作](https://hackmd.io/O6Wr6NlGRkazGnQw5BvDlg)
* [使用Dockerfile建立映像檔](https://hackmd.io/qv1CAU4_SsiSqcocEEjBFQ)
* [Django 心得記錄](https://hackmd.io/C996UN8HS52pKw81YcVb7g)
* [[Python] Process(程序)/Thread(執行緒)/GIL(全局解釋器鎖/Deadlock(死鎖))](https://hackmd.io/x2FGvGs3Rc-OGBODGHUqSg)
* [[Python] GC(Garbage Collection)垃圾回收機制/Middleware/JWT](https://hackmd.io/iD9Vd_RxS5WKeL8K7vtPxg)
* [[後端概念] Curl/WSGI/MVC/MTV](https://hackmd.io/XZWKlMw_Tgy3dBwMOgp2qA)
* [[後端概念] OSI七層協定/TCP四層協定/三次握手/四次揮手](https://hackmd.io/8VFqh1l5SQiS31Eu5SYBzQ)
* [[後端概念] 負載均衡/ACID/Http Cache/CORS](https://hackmd.io/4sJAJDbySQeqZge4N6z-XA)

### [My Blog](https://dysonma.github.io/)
* [[Python] asyncio/aiohttp - 非同步程式設計](https://dysonma.github.io/2021/01/27/python-asyncio-aiohttp-%E9%9D%9E%E5%90%8C%E6%AD%A5%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88/)
* [[Python] Unit Testing(單元測試)](https://dysonma.github.io/2021/01/27/Python-Unit-Testing-%E5%96%AE%E5%85%83%E6%B8%AC%E8%A9%A6/)
* [前端遊戲專案紀錄](https://dysonma.github.io/2020/11/21/frontend_game/)
* [[D3.js] 資料視覺化之前端神器](https://dysonma.github.io/2021/01/27/D3-js-%E8%B3%87%E6%96%99%E8%A6%96%E8%A6%BA%E5%8C%96%E4%B9%8B%E5%89%8D%E7%AB%AF%E7%A5%9E%E5%99%A8/)
* [[Node.js+Firebase] 報名網站專案心得](https://dysonma.github.io/2020/12/27/%E5%A0%B1%E5%90%8D%E7%B6%B2%E7%AB%99%E5%B0%88%E6%A1%88%E5%BF%83%E5%BE%97/)
* [[Node.js + Firebase] 全端網站開發-學習筆記](https://dysonma.github.io/2020/12/27/%E5%85%A8%E7%AB%AF%E7%B6%B2%E7%AB%99%E9%96%8B%E7%99%BC-%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98/)
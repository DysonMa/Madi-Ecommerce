# Madi-Ecommerce

* 這是一個用 Django, Bootstrap, MySQL(或SQLite), Docker 架設並部署在 Heroku 的購物網站。

![home](/static/githubImages/4.PNG)

## 功能
* 響應式(RWD)網站設計
* 首頁圖片輪播(Carousel)
* 使用者驗證(django auth)
* 第三方登入驗證(Google、GitHub)
* 將商品加入購物車並提交訂單(session)
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

* 註冊帳號，成功後會寄發註冊成功的電子郵件
<img src='/static/githubImages/17.PNG' width='750px'>
<img src='/static/githubImages/18.PNG' width='750px'>

* 登入後，進入首頁
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
client_secret = 

[MySQL]
client_secret = 
```

* `[Django] SECRET_KEY`: 可以不用編輯，因為是demo版，所以仍然附在code裡面
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

## 學習筆記



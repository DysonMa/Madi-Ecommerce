# Madi-Ecommerce

## 關於

* [English README.md(英文 README.md)](https://github.com/DysonMa/Madi-Ecommerce/blob/master/README.md)
* 這是一個用 Django, Bootstrap, MySQL, Docker 架設並部署在 Heroku 的購物網站。
* 帳號:madi | 密碼:840914

![home](/static/githubImages/4.PNG)

## 功能
* 響應式(RWD)網站設計
* 圖片輪播(Carousel)
* 使用者驗證(django auth)
* 第三方登入(Google、GitHub)
* 將商品加入購物車並提交訂單(session)
* 發送訂單確認的電子郵件給顧客(SMTP + Gmail)
* Admin管理後臺可以上傳產品圖片(django-filer)

## 使用技術與工具
* 前端:
    - HTML5
    - CSS3
    - jQuery
    - [Bootstrap(4.5.2)](https://getbootstrap.com/)
* 後端:
    - [Django(3.1.7)](https://www.djangoproject.com/)
        - session
        - form
        - email(SMTP+Gmail)
        - django-allauth  
* 資料庫:
    - [MySQL](https://www.mysql.com/)
    - [SQLite(地端測試)](https://www.sqlite.org/index.html)
* 部署:
    - [Docker](https://www.docker.com/)

## 演示步驟與展示圖片

* 尚未有帳號密碼，所以導至登入頁面
<img src='/static/githubImages/14.PNG' width='750px'>

* 第三方登入(Google、GitHub)
![login](/static/githubImages/15.PNG)
![login](/static/githubImages/16.PNG)

* 註冊帳號，成功後會寄發註冊成功的電子郵件
![register](/static/githubImages/17.PNG)
![register](/static/githubImages/18.PNG)

* 登入後，進入首頁
![home](/static/githubImages/4.PNG)

* 使用者個人資料
![userinfo](/static/githubImages/7.PNG)

* 分類檢視
![category](/static/githubImages/5.PNG)
![category](/static/githubImages/6.PNG)

* 選購商品，加入購物車
![cart](/static/githubImages/8.PNG)
![cart](/static/githubImages/9.PNG)
![cart](/static/githubImages/10.PNG)

* 按下"我要訂購"，並輸入訂購資訊
![order](/static/githubImages/11.PNG)
![order](/static/githubImages/12.PNG)

* 發送電子郵件通知訂單給顧客
![email](/static/githubImages/13.PNG)

* 想增加商品圖片，可以在Admin管理後臺上傳圖片
![upload](/static/githubImages/1.PNG)
![upload](/static/githubImages/2.PNG)

## 如何開始
### 安裝
遠端下載repo
```
git clone https://github.com/DysonMa/Madi-Ecommerce.git
```
## 使用


## 憑證
Distributed under the MIT License.

## 聯絡方式
Dyson Ma - madihsiang@gmail.com
Project Link: https://github.com/DysonMa/Madi-Ecommerce

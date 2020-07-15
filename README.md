# My Django Project

안녕하세요 개인프로젝트로 웹사이트를 만들고 있습니다. 웹크롤러를 통해 네이버 및 다음 IT 뉴스를 가져오고, 게시판을 통해 글을 쓰는 등의 작업을 하고 있습니다. 현재 뉴스의 타이틀과 링크만 가져오지만, 추후에 요약문도 가져 올 생각입니다.



### 구 성

- WEB Crawler
  - Using Beautiful Soup4
  - 다음 IT 뉴스 & 네이버 IT 뉴스 크롤링
- DB
  - Using MySQL



### 개발 환경

- Language
  - Python 3.8.3
- Platform
  - Django 3.0.8
- DB
  - MySQL
- CSS
  - Bootstrap 4.5.0



### 설치 및 실행

1. Download source from GitHub repositories:

```
mkdir git
cd git
git clone https://github.com/epicari/my_django.git
cd my_django
```

2. Create a Virtual environment:

```
python3 -m venv my_venv
```

3. On Windows, run:

```
my_venv\Scripts\Activate.ps1
```

- On Unix or MacOS, run:

```
source my_venv/bin/activate
```

- The name of the current virtual environment appears to the left of the prompt:

```
(my_venv) PS C:\>
```

4. Install Python packages:

```
(my_venv) pip install django, djangorestframework, bs4, requests, mysqlclient
```

5. MySQL Setting:

```
mysql> CREATE DATABASE news;
```

- Create account:

  ```
  mysql> CREATE USER 'djangouser'@'%' IDENTIFIED WITH mysql_native_password BY 'django1234';
  ```

- Access to the database:

  ```
  mysql > GRANT ALL ON news.* TO 'djangouser'@'%';
  ```

6. MySQL Connection to Application:

```
(my_venv) cd myproject
(my_venv) python .\manage.py makemigrations
(my_venv) python .\manage.py migrate
```

7. Run:

```
(my_venv) python web_crw_news_title.py #You have to do it first... 
(my_venv) python .\manage.py runserver
```



### 추가 할 기능들

- 게시판
- 뉴스에 대한 제목, 요약, 링크 및 사진 및 크롤러 자동실행
- 회원가입 및 로그인



### 참고

- [1] django (https://www.djangoproject.com/)
- [2] Django REST framework (https://www.django-rest-framework.org/)
- [3] How To Create a Django App and Connect it to a Database (https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database)


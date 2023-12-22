## Pythonの仮想環境を作成

```sh
cd ./02_url
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## Djangoプロジェクト作成

```sh
django-admin startproject url_proj
cd ./url_proj
python3 manage.py startapp url_app
python3 manage.py startapp request_app
python3 manage.py runserver
```

## HTTPリクエスト

新しいターミナルを開く

```sh
cd ./02_url
source venv/bin/activate
python3 request.py
```
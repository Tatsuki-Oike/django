## Pythonの仮想環境を作成

```sh
cd ./08_drf
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## Djangoプロジェクト作成

```sh
django-admin startproject drf_proj
cd ./drf_proj
python3 manage.py startapp task_api
```

## データベース設定

settings.pyにアプリ追加
modelにテーブルの内容記述

```sh
python3 manage.py makemigrations task_api
python3 manage.py migrate
python3 manage.py runserver
```

## テスト

新しいターミナル

```sh
cd ./08_drf
source venv/bin/activate
python3 request.py
```

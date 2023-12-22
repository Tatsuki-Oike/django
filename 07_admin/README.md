## Pythonの仮想環境を作成

```sh
cd ./07_admin
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## Djangoプロジェクト作成

```sh
django-admin startproject admin_proj
cd ./admin_proj
python3 manage.py startapp crud_app
python3 manage.py startapp user_app
```

## データベース設定

* settings.pyにアプリ追加
* modelにテーブルの内容記述

```sh
python3 manage.py makemigrations crud_app
python3 manage.py migrate
```

## スーパーユーザー作成

* admin.pyにmodelを追加

```sh
python manage.py createsuperuser
python3 manage.py runserver
```
## Pythonの仮想環境を作成

```sh
cd ./06_crud
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## Djangoプロジェクト作成

```sh
django-admin startproject crud_proj
cd ./crud_proj
python3 manage.py startapp crud_app
```

## データベース設定

* settings.pyにアプリ追加
* modelにテーブルの内容記述

```sh
python3 manage.py makemigrations crud_app
python3 manage.py migrate
python3 manage.py runserver
```
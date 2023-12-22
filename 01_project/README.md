## Pythonの仮想環境を作成

```sh
cd ./01_project
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## Djangoプロジェクト作成

```sh
django-admin startproject sample_proj
cd ./sample_proj
python3 manage.py runserver
```

## Djangoアプリ作成

```sh
python3 manage.py startapp sample_app
```

## 既存のプロジェクトを実行する

仮想環境に入った状態

```sh
cd ./01_project/hello_proj
python3 manage.py runserver
```
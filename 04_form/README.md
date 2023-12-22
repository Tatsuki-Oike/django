## Pythonの仮想環境を作成

```sh
cd ./04_form
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## Djangoプロジェクト作成

```sh
django-admin startproject form_proj
cd ./form_proj
python3 manage.py startapp form_app
python3 manage.py runserver
```
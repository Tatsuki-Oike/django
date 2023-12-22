## Pythonの仮想環境を作成

```sh
cd ./03_temp
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```


## Djangoプロジェクト作成

```sh
django-admin startproject temp_proj
cd ./temp_proj
python3 manage.py startapp temp_app
python3 manage.py runserver
```
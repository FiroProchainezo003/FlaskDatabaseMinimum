# FlaskDatabaseMinimum

## プロジェクトについて

このプロジェクトはFlaskでDB操作(SELECT)をする最小のサンプルです。
DB操作にはFlask-SQLAlchemyを使用しています。

# プロジェクトの取得方法

クローンしてください。

```
git clone https://github.com/FiroProchainezo003/FlaskDatabaseMinimum
```

## 実行方法

### windows

```shell script
# Cloneしたフォルダで
$ python3 -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
# ここで「DBの作成」「DBへのデータ入力」を実行
$ python app.py
```

上記が完了したらブラウザで `http://localhost:5000/` にアクセス

ログインID: a パスワード: a -> Login Error
ログインID: admin パスワード: password -> Login Success admin

### linux

```shell script
# Cloneしたフォルダで
$ python3 -m vevn venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
# ここで「DBの作成」「DBへのデータ入力」を実行
$ python app.py
```

## DBの作成

```python
# Linux / Windows 共通
# pythonインタープリターで実行
# python3
import os
os.mkdir('tmp')

from app import db
db.create_all()

```

## DBへのデータ入力

```python
# Linux / Windows共通
# pythonインタープリターで実行
# python3
from app import db, User
# DBの作成から連続で行う場合は `from app import User`
admin = User(user_id=1, login_id='admin', password='password')
user = User(user_id=2, login_id='user', password='password')
db.session.add(admin)
db.session.add(user)
db.session.commit()

```

## pythonバージョン

作成環境は python 3.8.3

## 各モジュールがサポートしているバージョン

### Flask
[Flask - 1.1.x Installation](https://flask.palletsprojects.com/en/1.1.x/installation/)

### FlaskSQLAlchemy
[FlaskSQLAlchemy - 2.x](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

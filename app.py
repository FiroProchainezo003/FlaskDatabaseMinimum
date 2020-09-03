from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column("userID", db.Integer, primary_key=True)
    login_id = db.Column("loginID", db.String)
    password = db.Column("password", db.String)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        try:
            user = db.session.query(User).filter(
                User.login_id == request.form['loginID'],
                User.password == request.form['password']
            ).first()
            if user is not None:
                return render_template('index.html', success=f'Login Success {user.login_id}')
            else:
                return render_template('index.html', error=f'Login Error')
        except Exception as e:
            print(f'Error {e}')
            return render_template('index.html', error=f'Error {e}')


if __name__ == '__main__':
    app.run()

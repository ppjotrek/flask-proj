from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

items = ["Pierwszy element", "Drugi element", "Trzeci element"]

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<User {self.first_name}>'
    

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        user = User(first_name=first_name)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        users = User.query.all()
        return render_template('index.html', users=users)
    
app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)
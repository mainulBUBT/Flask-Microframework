from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SelectField

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KET'] ='iammihan'

db = SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    state = db.Column(db.String(40))
    name = db.Column(db.String(40))



if __name__ == '__main__':
    app.run(debug=True)
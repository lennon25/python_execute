#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
# app.config.from_object(config)
app.config["SQLACHEMY_DATABASE_URI"] = "mysql+pymysql://root:lennon@localhost:3306/lennon"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

db = SQLAlchemy(app)

# db.create_all()

# class Student(db.Model):
# 	s_id = db.Column(db.Interger, primary_key=True, autoincrement=True)
# 	S_name = db.Column(db.String(20), unique=True)
# 	s_age = db.Column(db.Interger, default=18)
# 	s_grade= db.Column(db.Integer, db.ForeignKey("grade.g_id"), nullable=True)

# 	__tablename__ = "student"

# 	def __init__(self, name, age):
# 		self.s_name = name
# 		self.s_age = age



# class Grade(db.Model):
# 	g_id = db.Column(db.Interger, primary_key=True, autoincrement=True)
# 	g_name = db.Column(db.String(10), unique=True)
# 	g_desc = db.Column(db.String(100), nullable=True)
# 	g_time = db.Column(db.Date, default=datetime.now)


# 	__tablename__ = "grade"

# 	def __init__(self, name, desc):
# 		self.g_name = name
# 		self.s_desc = desc


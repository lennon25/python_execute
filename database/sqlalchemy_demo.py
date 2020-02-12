#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask
import pymysql
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:lennon@localhost:3306/lennon"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

db = SQLAlchemy(app)

class Article(db.Model):
	__tablename__ = "article"
	id = db.Column(db.Integer, primary_key = True, autoincrement= True)
	title = db.Column(db.String(100), nullable= False)
	content = db.Column(db.Text, nullable=False)


db.create_all()

@app.route("/")
def index():
	return "index"


# 增
article1 = Article(title= u"aaa", content=u"bbb")
db.session.add(article1)
db.session.commit()

# 查
article2 = Article.query.filter(Article.title == 'aaa').first()
print("title: %s" % article2.title)
print("content: %s" % article2.content)

# 改
article3 = Article.query.filter(Article.title == "aaa").first()
article3.title = "New title"
db.session.commit()

# 删
article4 = Article.query.filter(Article.title = "New title").first()
db.session.delete(article4)
db.session.commit()



if __name__ == "__main__":
	app.run(debug=True)



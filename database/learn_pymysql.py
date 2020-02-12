#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymysql

# 创建数据表 CREATE TABLE
db = pymysql.connect(host="localhost",user='root',password="lennon", database="lennon")
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS employee")
sql = """CREATE TABLE employee(first_name CHAR(20) NOT NULL,
		last_name CHAR(20),
		AGE INT,
		GENDER CHAR(1),
		INCOME FLOAT)"""
cursor.execute(sql)
db.close()


# 插入数据 INSERT INTO
db = pymysql.connect("localhost","root","lennon","lennon")
cursor = db.cursor()
sql = """INSERT INTO employee
	(first_name, last_name, AGE, GENDER, INCOME)
	VALUES
	("lennon","wang", 18, "F", 1800),
	("Mac","Mohan",20, "M", 3000),
	("lucy","Michl",24,"F", 2000),
	("abc", "Li",28, "F", 2500),
	("1111","2222", 22,"M", 3333)"""
try:
	cursor.execute(sql)
	# 提交到数据库执行！！！
	db.commit()
except:
	db.rollback()
db.close()


# 查询数据 SELECT ... FROM ... WHERE ...
db = pymysql.connect("localhost","root","lennon","lennon")
cursor = db.cursor()
sql = "SELECT * FROM employee \
	WHERE INCOME > %s" % (1000)
try:
	cursor.execute(sql)
	results = cursor.fetchall()
	for row in results:
		fname = row[0]
		lname = row[1]
		age = row[2]
		gender= row[3]
		income = row[4]
		print("fname=%s, lname=%s, age=%s, gender=%s, income=%s" % 
			(fname, lname, age, gender, income))
except:
	print("Error: unable to fetch data.")
db.close()


# 修改更新数据 UPDATE ... SET ... WHERE ...
db = pymysql.connect("localhost", "root","lennon","lennon")
cursor = db.cursor()
sql = """UPDATE employee SET first_name='rachel' WHERE last_name='Li'"""
try:
	cursor.execute(sql)
	db.commit()
	print("update success")
except:
	db.rollback()
	print("Error: update failure")
db.close()


# 删除数据 DELETE FORM ... WHERE ...
db = pymysql.connect("localhost","root","lennon", "lennon")
cursor = db.cursor()
sql = """DELETE FROM employee WHERE first_name='1111'"""
try:
	cursor.execute(sql)
	db.commit()
	print("delete success")
except:
	print("Error: delete failure")
db.close()


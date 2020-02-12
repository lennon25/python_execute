#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymysql

def chinese_output(str_tuple):
	for i in range(len(str_tuple)):
		print(str_tuple[i])
	pass


class MySQLSearch(object):
	
	def __init__(self):
		pass


	def get_conn(self):
		try:
			self.conn = pymysql.connect(
				host="localhost",
				user="root",
				password="lennon",
				db="news",
				port=3306,
				charset="utf-8")
		except pymysql.Error as e:
			print("Error: %s" % e)

	def close_conn(self):
		try:
			if self.conn:
				self.conn.close()
		except pymysql.Error as e:
			print("Error: %s" % e)

	def create_table(self):
		cursor = self.conn.cursor()
		cursor.execute("DROP TABLE IF EXISTS NEWS")
		sql = """CREATE TABLE news (title VARCHAR(200) NOT NULL,
				image VARCHAR(200) NULL,
				content VARCHAR(400) NOT NULL,
				type VARCHAR(100) NULL,
				is_valid INT OR VARCHAR(200) NOT NULL,
				created_at DATETIME NOT NULL)"""
		try:
			cursor.execute(sql)
			self.conn.commit()
		except Ecception as e:
			print("Error: %s" % e)
			self.conn.rallback()
		self.conn.close()

	def get_one(self):
		sql = "SELECT * FROM news WHERE type = %s ORDERY BY create_at DESC"
		cursor = self.conn.cursor()
		cursor.execute(sql, ("本地",))
		rest = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
		print(rest)
		cursor.close()
		self.close_conn()
		return rest









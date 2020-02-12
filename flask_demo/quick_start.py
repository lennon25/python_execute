#!/usr/bin/env python3

# flask最小应用
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
# 	return "Hello, World!"


# if __name__ == '__main__':
# 	app.run()


# 构造URL
from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def index():
	pass

@app.route("/login")
def login():
	pass

@app.route("/user/<username>")
def profile(username):
	pass


with app.test_request_context():
	print(url_for("index"))
	print(url_for("login"))
	print(url_for("login", next="/"))
	print(url_for("profile", username= "Lennon wang"))
	print(url_for("static", filename="style.css"))  # 静态文件生成URL


# # HTTP方法
# #通过 route()装饰器传递 methods参数
# @app.route("/login", methods=["GET", "POST"])
# def login():
# 	if request.method =="POST":
# 		do_the_login()
# 	else:
# 		show_the_login_form()


# 请求对象实例
@app.route("/login", methods=["POST", "GET"])
def login():
	error = None
	if request.method == "POST":
		if valid_login(request.form["username"],
			request.form["password"]):
			return log_the_user_in(request.form["username"])
		else:
			error = "Invalid username/password"
	return render_template("login.html", error=error)






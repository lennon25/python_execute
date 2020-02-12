
# from flask import Flask
# import flask_restful

# flask restful MVP
# app = Flask(__name__)
# api = flask_restful.Api(app)


# class HelloWorld(flask_restful.Resource):
# 	def get(self):
# 		return {"Hello": "world"}


# api.add_resource(HelloWorld, "/")


# if __name__ == "__main__":
# 	app.run(debug=True)


# restful API CRUD(增删改查)
# from flask import Flask, request
# from flask_restful import Resource, Api

# app = Flask(__name__)
# api = Api(app)

# todos = {}

# class TodoSimple(Resource):
# 	def get(self, todo_id):
# 		return {todo_id : todos[todo_id]}

# 	def post(self, todo_id):
# 		todos[todo_id] = request.form["data"]
# 		return {todo_id: todos[todo_id]}

# 	def put(self, todo_id):
# 		if todos[todo_id]:
# 			todos[todo_id] = request.form["data"]
# 			return {todo_id: todos[todo_id]}
# 		else:
# 			return ""


# api.add_resource(TodoSimple, "/<string:todo_id>")


# if __name__ == "__main__":
# 	app.run(debug=True)

# test
# curl http://localhost:5000/todo1 -d "data="I have money" -X POST


# 支持多种返回值
# class Todo1(Resource):
# 	def get(self):
# 		return {"task": "Hello, World!"}

# class Todo2(Resource):
# 	def get(self):
# 		return {"task": "Hello,World"}, 200

# class Todo3(Resource):
# 	def get(self):
# 		return {"task": "Hello,World"}, 201, {"Etag": "some-opaque-string"}

# # api.add_resource(Todo, "/todo/<int:todo>", endpoint="todo_ep")

# # 参数解析
# from flask_restful import reqparse
# parser = reqparse.RequestParser()
# parser.add_argument("rate", type=int, help="Rate to charge for this resource")
# args = parser.parse_args()


# 数据格式化
# from collections import OrderedDict
# from flask_restful import fields, marshal_with

# resource_fields = {
# 	"task": fields.String,
# 	"url": fields.Url("todo_ep")
# }

# class TodoDao(object):
# 	def __init__(self, todo_id, task):
# 		self.todo_id = todo_id
# 		self.task = task
# 		self.status = "active"

# class Todo(Resource):
# 	@marshal_with(resource_fields)
# 	def get(self, *args, **kw):
# 		return TodoDao(todo_id="my_todo", task="Remember the milk.")



# 数据格式化， 完整的实例
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)


TODOS = {
	"todo1": {"task": "build an API"},
	"todo2": {"task": "?????"},
	"todo3": {"task": "profit!"}
}

def abort_if_todo_doesnt_exist(todo_id):
	if todo_id not in TODOS:
		abort(404,message="Todo {} doesn't exist".format(todo_id))


parser = reqparse.RequestParser()
parser.add_argument("task", type= str)

# Todo
class Todo(Resource):
	def get(self, todo_id):
		abort_if_todo_doesnt_exist(todo_id)
		return TODOS[todo_id]

	def delete(self, todo_id):
		abort_if_todo_doesnt_exist(todo_id)
		del TODOS[todo_id]
		return "", 204

	def put(self, todo_id):
		args = parser.parse_args()
		task = {"task": args["task"]}
		TODOS[todo_id] = task
		return task, 201

# TodoList
class TodoList(Resource):
	def get(self):
		return TODOS

	def post(self):
		args = parser.parse_args()
		todo_id = int(max(TODOS.keys()).lstrip("todo")) + 1
		todo_id = "todo%i" % todo_id
		TODOS[todo_id] = {"task": args["task"]}
		return TODOS[todo_id], 201



api.add_resource(Todo, "/todos/<todo_id>")
api.add_resource(TodoList, "/todos")

if __name__ == "__main__":
	app.run(debug=True)

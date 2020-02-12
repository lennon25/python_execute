
# 参数解析
from flask_restful import reqparse

parser = reqparse.Reqparse()
parser.add_argument("rate", type=int, helep="Rate cannot be converted")
parser.add_argument("name", type=str)
args = parser.parse_args()
# args["name"]

# 必需参数
parser.add_argument("name", type=str, required=True, help="Name connot be blank")
# 列表参数
parser.add_argument("name", type=str, action="append")


# 继承解析
form falsk_restful import RequestParser

parser = RequestParser()
parser.add_argument("foo", type=int)

parser_copy = parser.copy()
parser_copy.add_argument("bar", type=int)

parser_copy.replace_argument("foo",type=str, required=True, location="json")






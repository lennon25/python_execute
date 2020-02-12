
def application(environ, start_response):
	start_response("200 ok", [("Content-Type","text/html")])
	body = "<b>Hello, %s!</b>" % (environ["PATH_INFO"][1:] or "web")
	return [body.encode("utf-8")]

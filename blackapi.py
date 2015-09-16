import inspect
import os
from bottle import route, run, request, default_app, static_file, error, abort
from bottleutils import checkAccceptIsJson, parseObjectToJson, checkContentIsJson, parseJsonToObject
from helloworld import HelloWorld

#Web

@route('/')
def serve_homepage():
    return serve_static("index.html");

@route('/<filename>')
def serve_static(filename):
    return static_file(filename, root="static");

@route('/style/<filename>')
def styles(filename):
    return static_file(filename, root="style")


@error(404)
def error404(error):
    return serve_static("error404.html")

#Rest Services

@route('/hello', method='GET')
def hello():
    hello = HelloWorld()
    if checkAccceptIsJson(request):
        return parseObjectToJson(hello)
    else:
        return abort(404)

@route('/hello', method='POST')
def hello():
    if checkAccceptIsJson(request) and checkContentIsJson(request):
        hello = HelloWorld.fromJson(parseJsonToObject(request))
        return parseObjectToJson(hello)
    else:
        return abort(404)

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
else:
    application = default_app()

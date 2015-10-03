from time import time
from bottle import route, run, request, default_app, error, abort, hook, response

from bottleutils import checkAcceptIsJson, parseObjectToJson, checkContentIsJson, parseJsonToObject, setResponseContentTypeJson, \
    getAccept
from objects.error import Error
from objects.helloworld import HelloWorld
from objects.mathoperation import MathOperation


#Web
from objects.timeobject import TimeObject


@error(404)
def error404(error):
    if checkAcceptIsJson(request):
        return parseObjectToJson(Error())
    ##else:
        #redirect("http://api.blackleg.es/error404.html")

"""@hook('before_request')
def before_request():
    print("Before Request")
    print(request.content_type)"""

@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type'


#Rest Services

@route('/<method>', method='OPTIONS')
def options(method):
    return


@route('/status', method='GET')
def hello():
    if checkAcceptIsJson(request):
        return {'status': True}
    else:
        return abort(404)

@route('/hello', method='GET')
def hello():
    if checkAcceptIsJson(request):
        setResponseContentTypeJson(response)
        hello = HelloWorld()
        return parseObjectToJson(hello)
    else:
        return abort(404)

@route('/hello', method='POST')
def hello():
    if checkAcceptIsJson(request) and checkContentIsJson(request):
        hello = HelloWorld.fromJson(parseJsonToObject(request))
        return parseObjectToJson(hello)
    else:
        return abort(404)

"""@route('/quoteoftheday', method='GET')
def quoteoftheday():
    hello = HelloWorld()
    if checkAccceptIsJson(request):
        return parseObjectToJson(hello)
    else:
        return abort(404)

@route('/quoteoftheday', method='POST')
def quoteoftheday():
    hello = HelloWorld()
    if checkAccceptIsJson(request):
        return parseObjectToJson(hello)
    else:
        return abort(404)
"""

@route('/math', method='POST')
def getmath():
    if checkAcceptIsJson(request) and checkContentIsJson(request):
        return parseObjectToJson(MathOperation.fromJson(parseJsonToObject(request)))
    else:
        return abort(404)

@route('/time', method='GET')
def gettime():
    if checkAcceptIsJson(request):
        setResponseContentTypeJson(response)
        return parseObjectToJson(TimeObject(time()))
    else:
        return abort(404)


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
else:
    application = default_app()

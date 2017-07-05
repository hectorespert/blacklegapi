from time import time

from bottle import route, run, request, default_app, error, abort, hook, response, redirect
from datetime import date

from utilities.bottle import checkAcceptIsJson, checkContentIsJson, setResponseContentTypeJson, parseRequestToJson
from objects.error import Error
from objects.helloworld import HelloWorld
from objects.mathoperation import MathOperation

import logging

logger = logging.getLogger('api')


# Web
#from objects.model import initModel, closeModel, connectModel, QuoteOfDay, parseModelToJson
from objects.timeobject import TimeObject

# Init
from utilities.json import parseObjectToJson

#initModel()


@error(404)
def error404(error):
    return parseObjectToJson(Error())
        # redirect("http://api.blackleg.es/error404.html")


@hook('before_request')
def before_request():
    logger.info("Before request")
    #connectModel()


@hook('after_request')
def after_request():
    logger.info("After request")
    #closeModel()
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type'


# Rest Services

@route('/<method>', method='OPTIONS')
def options(method):
    return


@route('/', method='GET')
def root():
    redirect("https://www.blackleg.es")


@route('/status', method='GET')
def hello():
    if checkAcceptIsJson(request):
        return {'status': True}
    else:
        return abort(404)


#@route('/hello', method='GET')
#def hello():
    #if checkAcceptIsJson(request):
        #setResponseContentTypeJson(response)
        #hello = HelloWorld()
        #return parseObjectToJson(hello)
    #else:
        #return abort(404)


#@route('/hello', method='POST')
#def hello():
    #if checkAcceptIsJson(request) and checkContentIsJson(request):
        #setResponseContentTypeJson(response)
        #hello = HelloWorld.fromJson(parseRequestToJson(request))
        #return parseObjectToJson(hello)
    #else:
        #return abort(404)


#@route('/quoteoftheday', method='GET')
#def quoteoftheday():
    #if checkAcceptIsJson(request):
        #setResponseContentTypeJson(response)
        #quote = QuoteOfDay.get(QuoteOfDay.id == 1)
        #return parseModelToJson(quote)
    #else:
        #return abort(404)


#@route('/quoteoftheday', method='POST')
#def quoteoftheday():
    #if checkAcceptIsJson(request) and checkContentIsJson(request):
        #setResponseContentTypeJson(response)
        #json = parseRequestToJson(request)
        #updatedQuote = QuoteOfDay.update(author = json['author'], quote = json['quote'], date = date.today().isoformat()).where(QuoteOfDay.id == 1)
        #updatedQuote.execute()
    #else:
        #return abort(404)


#@route('/math', method='POST')
#def getmath():
    #if checkAcceptIsJson(request) and checkContentIsJson(request):
        #setResponseContentTypeJson(response)
        #return parseObjectToJson(MathOperation.fromJson(parseRequestToJson(request)))
    #else:
        #return abort(404)


@route('/timestamp', method='GET')
def gettimestamp():
    if checkAcceptIsJson(request):
        setResponseContentTypeJson(response)
        return parseObjectToJson(TimeObject(time()))
    else:
        return abort(404)


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
else:
    application = default_app()

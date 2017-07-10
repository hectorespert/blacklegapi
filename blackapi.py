from time import time

from bottle import route, run, default_app, error, hook, response

from utilities.bottle import setResponseContentTypeJson
from objects.error import Error
from objects.timeobject import TimeObject
from objects.status import Status
from utilities.json import parseToJson
import logging

logger = logging.getLogger('api')


@error(404)
def error404(error):
    return parseToJson(Error())


@hook('before_request')
def before_request():
    logger.info("Before request")


@hook('after_request')
def after_request():
    logger.info("After request")
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type'


@route('/<method>', method='OPTIONS')
def options(method):
    return


@route('/', method='GET')
@route('/status', method='GET')
def status():
    setResponseContentTypeJson(response)
    return parseToJson(Status())


@route('/time', method='GET')
def gettimestamp():
    setResponseContentTypeJson(response)
    return parseToJson(TimeObject(time()))


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
else:
    application = default_app()

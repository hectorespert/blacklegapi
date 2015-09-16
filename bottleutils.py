__author__ = 'Blackleg'
import json
from xml.dom.minidom import parse

appxml = "application/xml"
appjson = "application/json"
appplain = "text/plain"


def getAccept(request):
    return request.headers.get("Accept")

def checkAccceptIsXml(request):
    return getAccept(request) == appxml

def checkAccceptIsJson(request):
    return getAccept(request) == appjson

def checkAccceptIsPlain(request):
    return getAccept(request) == appplain

def checkContentIsJson(request):
    return request.content_type == appjson

def parseObjectToJson(object):
    return json.dumps(object.__dict__)

def parseObjectToXml(object):
    return parse(object.__dict__)

def parseJsonToObject(request):
    return request.json



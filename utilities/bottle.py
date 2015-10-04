
__author__ = 'Blackleg'

appall = "*/*"
appxml = "application/xml"
appjson = "application/json"
appplain = "text/plain"


def getAccept(request):
    return request.get_header("Accept")

def checkIfAcceptAll(request):
    accept = getAccept(request)
    if appall in accept:
        return True
    else:
        return False

def checkIfAcceptContainApp(request, app):
    accept = getAccept(request)
    if app in accept or checkIfAcceptAll(request):
        return True
    else:
        return False

def checkAcceptIsXml(request):
    return checkIfAcceptContainApp(request, appxml)

def checkAcceptIsJson(request):
    return checkIfAcceptContainApp(request, appjson)

def checkAcceptIsPlain(request):
    return checkIfAcceptContainApp(request, appplain)

def getContentType(request):
    return request.content_type;

def checkContentIs(request, app):
    if app in getContentType(request):
        return True
    else:
        return False

def checkContentIsJson(request):
    return checkContentIs(request, appjson)

def setResponseContentType(response, type):
    response.content_type = type

def setResponseContentTypeJson(response):
    setResponseContentType(response, appjson)


def parseRequestToJson(request):
    return request.json
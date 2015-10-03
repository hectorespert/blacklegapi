__author__ = 'Blackleg'


class HelloWorld:

    def __init__(self, hello="Hello World"):
        self.hello = hello

    @staticmethod
    def fromJson(json):
        return HelloWorld(**json)
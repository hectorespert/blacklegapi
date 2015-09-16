__author__ = 'Blackleg'


class HelloWorld:

    def __init__(self):
        self.hello="Hello World"

    def __init__(self, hello):
        self.hello = hello



    @staticmethod
    def fromJson(json):
        return HelloWorld(**json)
__author__ = 'hector'

class Error:

    def __init__(self):
        self.message = "Not Found"
        self.error = "404"

    @staticmethod
    def fromJson(json):
        return Error(**json)
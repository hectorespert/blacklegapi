__author__ = 'Blackleg'

class Quote:

    def __init__(self, author="Pepe", quote="Quote of the day"):
        self.author = author
        self.quote = quote

    @staticmethod
    def fromJson(json):
        return Quote(**json)
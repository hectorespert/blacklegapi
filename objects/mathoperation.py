__author__ = 'Blackleg'


class MathOperation:

    def __init__(self, operation, firstnumber, secondnumber):
        self.operation = operation
        self.firstnumber = firstnumber
        self.secondnumber = secondnumber
        self.result = MathOperation.calculate(operation, firstnumber, secondnumber)


    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b;

    def divide(a, b):
        return a / b

    @staticmethod
    def fromJson(json):
        return MathOperation(**json)

    @staticmethod
    def calculate(operation, firstnumber, secondnumber):
        operations = { 'add': MathOperation.add, 'subtract': MathOperation.subtract, 'multiply': MathOperation.multiply, 'divide': MathOperation.divide}
        return operations[operation](firstnumber, secondnumber)




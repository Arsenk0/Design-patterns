# bridge.py

class Implementor:
    def operation(self):
        pass

class ConcreteImplementorA(Implementor):
    def operation(self):
        return "ConcreteImplementorA: operation."

class ConcreteImplementorB(Implementor):
    def operation(self):
        return "ConcreteImplementorB: operation."

class Abstraction:
    def __init__(self, implementor: Implementor):
        self.implementor = implementor

    def operation(self):
        return self.implementor.operation()

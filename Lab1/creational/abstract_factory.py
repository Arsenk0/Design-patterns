class AbstractProductA:
    def operation(self):
        return "AbstractProductA operation"

class ConcreteProductA(AbstractProductA):
    def operation(self):
        return "ConcreteProductA from AbstractFactory"

class AbstractFactory:
    def create_product_a(self):
        return ConcreteProductA()
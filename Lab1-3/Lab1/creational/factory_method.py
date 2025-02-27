class Product:
    def operation(self):
        return "Product operation"

class ConcreteProductA(Product):
    def operation(self):
        return "ConcreteProductA operation"

class Factory:
    def create_product(self, product_type):
        if product_type == "A":
            return ConcreteProductA()
        else:
            return Product()

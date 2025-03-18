class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        return ", ".join(self.parts)

class Builder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def get_product(self):
        pass

class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add("PartA")

    def build_part_b(self):
        self.product.add("PartB")

    def get_product(self):
        return self.product

class Director:
    def __init__(self, builder):
        self._builder = builder

    def build_full_featured_product(self):
        self._builder.build_part_a()
        self._builder.build_part_b()
        return self._builder.get_product()
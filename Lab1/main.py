from Lab1.creational.singleton import Singleton
from Lab1.creational.factory_method import Factory
from Lab1.creational.abstract_factory import AbstractFactory
from Lab1.creational.builder import Director, ConcreteBuilder
from Lab1.creational.prototype import Prototype

def main():
    singleton1 = Singleton()
    singleton2 = Singleton()
    print(f"Singleton works: {singleton1 is singleton2}")

    factory = Factory()
    product = factory.create_product("A")
    print(product.operation())

    abstract_factory = AbstractFactory()
    productA = abstract_factory.create_product_a()
    print(productA.operation())

    builder = ConcreteBuilder()
    director = Director(builder)
    product = director.build_full_featured_product()
    print(f"Built product parts: {product.list_parts()}")

    prototype = Prototype("Prototype1")
    cloned = prototype.clone()
    print(f"Cloned prototype: {cloned.name}")

if __name__ == "__main__":
    main()
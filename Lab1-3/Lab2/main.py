# main.py

from structural.adapter import Adapter, Adaptee, Target
from structural.bridge import ConcreteImplementorA, ConcreteImplementorB, Abstraction
from structural.composite import Leaf, Composite
from structural.decorator import ConcreteComponent, Decorator
from structural.facade import Facade
from structural.flyweight import ConcreteFlyweight
from structural.proxy import Proxy, RealSubject

def main():
    # Adapter
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    print(adapter.request())

    # Bridge
    implementor_a = ConcreteImplementorA()
    implementor_b = ConcreteImplementorB()
    abstraction_a = Abstraction(implementor_a)
    abstraction_b = Abstraction(implementor_b)
    print(abstraction_a.operation())
    print(abstraction_b.operation())

    # Composite
    leaf = Leaf()
    composite = Composite()
    composite.add(leaf)
    print(composite.operation())

    # Decorator
    component = ConcreteComponent()
    decorated_component = Decorator(component)
    print(decorated_component.operation())

    # Facade
    facade = Facade()
    print(facade.operation())

    # Flyweight
    flyweight = ConcreteFlyweight()
    print(flyweight.operation("external state"))

    # Proxy
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    print(proxy.request())

if __name__ == "__main__":
    main()

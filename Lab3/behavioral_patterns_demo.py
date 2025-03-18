# behavioral_patterns_demo.py

from behavioral.command import LightOnCommand, Light
from behavioral.iterator import Iterator
from behavioral.chain_of_responsibility import ConcreteHandlerA, ConcreteHandlerB
from behavioral.interpreter import TerminalExpression, NonTerminalExpression
from behavioral.mediator import ConcreteMediator, Colleague
from behavioral.memento import Originator
from behavioral.observer import ConcreteObserver, Subject
from behavioral.state import ConcreteStateA, ConcreteStateB, Context
from behavioral.strategy import ConcreteStrategyA, ConcreteStrategyB, Context as StrategyContext
from behavioral.visitor import ConcreteVisitor, Element

def demo_chain_of_responsibility():
    handler = ConcreteHandlerA(ConcreteHandlerB())
    handler.handle_request("B")

def demo_command():
    light = Light()
    light_on = LightOnCommand(light)
    light_on.execute()

def demo_iterator():
    collection = [1, 2, 3, 4]
    iterator = Iterator(collection)
    while iterator.has_next():
        print(iterator.next())

def demo_mediator():
    colleague1 = Colleague(None)
    colleague2 = Colleague(None)
    mediator = ConcreteMediator(colleague1, colleague2)
    colleague1.send("Hello, Colleague 2!")

def demo_memento():
    originator = Originator()
    originator.set_state("State1")
    saved_state = originator.save_state_to_memento()
    originator.set_state("State2")
    print("Current state:", originator.state)
    originator.restore_state_from_memento(saved_state)
    print("Restored state:", originator.state)

def demo_observer():
    subject = Subject()
    observer1 = ConcreteObserver()
    subject.add_observer(observer1)
    subject.notify_observers("Hello, Observers!")

def demo_state():
    context = Context(ConcreteStateA())
    context.request()
    context.set_state(ConcreteStateB())
    context.request()

def demo_strategy():
    context = StrategyContext(ConcreteStrategyA())
    context.execute_strategy()
    context.set_strategy(ConcreteStrategyB())
    context.execute_strategy()

def demo_visitor():
    element = Element()
    visitor = ConcreteVisitor()
    element.accept(visitor)

# Демонстрація кожного патерну:
if __name__ == "__main__":
    print("Demonstrating Chain of Responsibility")
    demo_chain_of_responsibility()

    print("\nDemonstrating Command Pattern")
    demo_command()

    print("\nDemonstrating Iterator Pattern")
    demo_iterator()

    print("\nDemonstrating Mediator Pattern")
    demo_mediator()

    print("\nDemonstrating Memento Pattern")
    demo_memento()

    print("\nDemonstrating Observer Pattern")
    demo_observer()

    print("\nDemonstrating State Pattern")
    demo_state()

    print("\nDemonstrating Strategy Pattern")
    demo_strategy()

    print("\nDemonstrating Visitor Pattern")
    demo_visitor()

# decorator.py

class Component:
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent: operation."

class Decorator(Component):
    def __init__(self, component: Component):
        self.component = component

    def operation(self):
        return f"Decorator: {self.component.operation()}"

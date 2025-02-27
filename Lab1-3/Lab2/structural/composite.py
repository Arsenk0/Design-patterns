# composite.py

class Component:
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Leaf: operation."

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component: Component):
        self.children.append(component)

    def operation(self):
        result = "Composite: operation.\n"
        for child in self.children:
            result += child.operation() + "\n"
        return result

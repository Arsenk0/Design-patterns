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
#Composite дозволяє працювати з деревом об'єктів, де об'єкти можуть бути як одиничними елементами (листами)
# так і складними (композитами), при цьому клієнт взаємодіє з усіма елементами однаково.
class Visitor:
    def visit(self, element):
        pass

class ConcreteVisitor(Visitor):
    def visit(self, element):
        print(f"Visiting {element}")

class Element:
    def accept(self, visitor):
        visitor.visit(self)

# Demo
element = Element()
visitor = ConcreteVisitor()
element.accept(visitor)

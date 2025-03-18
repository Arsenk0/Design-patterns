class State:
    def handle(self):
        pass

class ConcreteStateA(State):
    def handle(self):
        print("Handling in State A")

class ConcreteStateB(State):
    def handle(self):
        print("Handling in State B")

class Context:
    def __init__(self, state: State):
        self.state = state

    def set_state(self, state: State):
        self.state = state

    def request(self):
        self.state.handle()

# Demo
context = Context(ConcreteStateA())
context.request()
context.set_state(ConcreteStateB())
context.request()

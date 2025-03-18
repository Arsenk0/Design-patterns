class Strategy:
    def execute(self):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self):
        print("Executing Strategy A")

class ConcreteStrategyB(Strategy):
    def execute(self):
        print("Executing Strategy B")

class Context:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def execute_strategy(self):
        self.strategy.execute()

# Demo
context = Context(ConcreteStrategyA())
context.execute_strategy()
context.set_strategy(ConcreteStrategyB())
context.execute_strategy()

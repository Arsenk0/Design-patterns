# flyweight.py

class Flyweight:
    def operation(self, extrinsic_state):
        pass

class ConcreteFlyweight(Flyweight):
    def operation(self, extrinsic_state):
        return f"ConcreteFlyweight: operation with state {extrinsic_state}."

#Flyweight використовує спільне використання об'єктів для оптимізації використання пам'яті,
# особливо коли об'єкти мають однаковий стан і ці об'єкти створюються багаторазово.


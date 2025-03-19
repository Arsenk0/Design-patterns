# facade.py

class SubsystemA:
    def operation_a(self):
        return "SubsystemA: operation."

class SubsystemB:
    def operation_b(self):
        return "SubsystemB: operation."

class Facade:
    def __init__(self):
        self.subsystem_a = SubsystemA()
        self.subsystem_b = SubsystemB()

    def operation(self):
        return f"Facade: {self.subsystem_a.operation_a()} {self.subsystem_b.operation_b()}"

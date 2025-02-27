class Memento:
    def __init__(self, state):
        self.state = state

class Originator:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def save_state_to_memento(self):
        return Memento(self.state)

    def restore_state_from_memento(self, memento):
        self.state = memento.state

# Demo
originator = Originator()
originator.set_state("State1")
saved_state = originator.save_state_to_memento()
originator.set_state("State2")
print("Current state:", originator.state)
originator.restore_state_from_memento(saved_state)
print("Restored state:", originator.state)

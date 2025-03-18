class Observer:
    def update(self, message):
        pass

class ConcreteObserver(Observer):
    def update(self, message):
        print(f"Observer received message: {message}")

class Subject:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

# Demo
subject = Subject()
observer1 = ConcreteObserver()
subject.add_observer(observer1)
subject.notify_observers("Hello, Observers!")

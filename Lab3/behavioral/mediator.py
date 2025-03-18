class Mediator:
    def send(self, message, colleague):
        pass

class ConcreteMediator(Mediator):
    def __init__(self, colleague1, colleague2):
        self.colleague1 = colleague1
        self.colleague2 = colleague2

    def send(self, message, colleague):
        if colleague == self.colleague1:
            self.colleague2.receive(message)
        else:
            self.colleague1.receive(message)

class Colleague:
    def __init__(self, mediator):
        self.mediator = mediator

    def send(self, message):
        self.mediator.send(message, self)

    def receive(self, message):
        print(f"Received message: {message}")

# Demo
mediator = ConcreteMediator(Colleague(None), Colleague(None))
colleague1 = Colleague(mediator)
colleague2 = Colleague(mediator)
colleague1.send("Hello, Colleague 2!")

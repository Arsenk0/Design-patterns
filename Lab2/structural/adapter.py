# adapter.py

class Target:
    def request(self):
        return "Target: The default behavior."

class Adaptee:
    def specific_request(self):
        return "Adaptee: Specific request."

class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return self.adaptee.specific_request()
#Adapter дозволяє змінити інтерфейс одного класу,щоб він став сумісним з іншим класом,не змінюючи його структуру.
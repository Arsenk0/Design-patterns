class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if self.successor:
            self.successor.handle_request(request)

class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request == "A":
            print("Handler A handled the request.")
        elif self.successor:
            self.successor.handle_request(request)

class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == "B":
            print("Handler B handled the request.")
        elif self.successor:
            self.successor.handle_request(request)

# Demo
handler = ConcreteHandlerA(ConcreteHandlerB())
handler.handle_request("B")

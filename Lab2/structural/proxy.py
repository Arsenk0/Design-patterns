# proxy.py

class Subject:
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        return "RealSubject: request."

class Proxy(Subject):
    def __init__(self, real_subject: RealSubject):
        self.real_subject = real_subject

    def request(self):
        return f"Proxy: {self.real_subject.request()}"

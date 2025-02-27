class Expression:
    def interpret(self):
        pass

class TerminalExpression(Expression):
    def interpret(self):
        return "Terminal Expression"

class NonTerminalExpression(Expression):
    def interpret(self):
        return "Non-Terminal Expression"

# Demo
expr1 = TerminalExpression()
expr2 = NonTerminalExpression()
print(expr1.interpret())
print(expr2.interpret())

#! /usr/bin/python3

class Forth:
    def __init__(self):
        self.stack = []

    def execute(self, input_str):
        words = input_str.split()

        for word in words:
            if word.isdigit():
                self.stack.append(int(word))
            elif word == '+':
                if len(self.stack) < 2:
                    print("Error: Not enough operands for addition.")
                    return
                else:
                    operand2 = self.stack.pop()
                    operand1 = self.stack.pop()
                    result = operand1 + operand2
                    self.stack.append(result)

        if self.stack:
            print("Result:", self.stack[-1])
        else:
            print("Stack is empty.")

interpreter = Forth()
interpreter.execute("5 3 +")

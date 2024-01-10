#! /usr/bin/python3

stack = []

def execute(input_str):
    words = input_str.split()

    for word in words:
        if word.isdigit():
            stack.append(int(word))
        elif word == '+':
            if len(stack) < 2:
                print(f"Error: Not enough operands for: {word}")
                return
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operand1 + operand2
                stack.append(result)
        elif word == '-':
            if len(stack) < 2:
                print(f"Error: Not enough operands for: {word}")
                return
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operand1 - operand2
                stack.append(result)
        elif word == '*':
            if len(stack) < 2:
                print(f"Error: Not enough operands for: {word}")
                return
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operand1 * operand2
                stack.append(result)
        elif word == '/':
            if len(stack) < 2:
                print(f"Error: Not enough operands for: {word}")
                return
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operand1 / operand2
                stack.append(result)

        elif word == '.':
            if stack:
                print(stack.pop())
            else:
                print("Stack is empty.")
        else:
            print("Unknown word:", word)

while True:
    input_str = input("Forth> ")
    if input_str.lower() == 'quit':
        break
    execute(input_str)

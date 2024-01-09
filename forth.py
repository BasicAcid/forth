#! /usr/bin/python3

stack = []

def execute(input_str):
    words = input_str.split()

    for word in words:
        if word.isdigit():
            stack.append(int(word))
        elif word == '+':
            if len(stack) < 2:
                print("Error: Not enough operands for addition.")
                return
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operand1 + operand2
                stack.append(result)
        elif word == '-':
            if len(stack) < 2:
                print("Error: Not enough operands for addition.")
                return
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operand1 - operand2
                stack.append(result)
        elif word == '*':
            if len(stack) < 2:
                print("Error: Not enough operands for addition.")
                return
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operand1 * operand2
                stack.append(result)
        elif word == '/':
            if len(stack) < 2:
                print("Error: Not enough operands for addition.")
                return
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operand1 / operand2
                stack.append(result)

    if stack:
        print("Result:", stack[-1])
    else:
        print("Stack is empty.")

execute("5 3 +")
execute("5 3 -")
execute("5 3 *")
execute("5 3 /")

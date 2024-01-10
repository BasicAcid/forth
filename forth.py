#! /usr/bin/python3

stack = []
definitions = {}


def bin_op(stack, word):

    if len(stack) < 2:
        print(f"Error: Not enough args for: {word}")
        return

    op_2 = stack.pop()
    op_1 = stack.pop()

    if word == "+":
        return stack.append(op_1 + op_2)
    elif word == "-":
        return stack.append(op_1 - op_2)
    elif word == "*":
        return stack.append(op_1 * op_2)
    elif word == "/":
        return stack.append(op_1 // op_2)

def dup(stack):
    if stack:
        top_element = stack[-1]
        stack.append(top_element)
    else:
        print("dup fail: Stack is empty.")

def drop(stack):
    if stack:
        stack.pop()
    else:
        print("drop fail: Stack is empty.")

def swap(stack):
    if len(stack) < 2:
        print(f"Error: Not enough args for: swap")
    else:
        stack[-1], stack[-2] = stack[-2], stack[-1]

def over(stack):
    if len(stack) < 2:
        print(f"Error: Not enough args for: over")
    else:
        stack.append(stack[-2])

def rot(stack):
    if len(stack) < 3:
        print(f"Error: Not enough args for: rot")
    else:
        stack[-3], stack[-2], stack[-1] = stack[-2], stack[-1], stack[-3]

def execute(input_str):

    words = input_str.split()

    i = 0
    while i < len(words):
        word = words[i]

        if word.isdigit():
            stack.append(int(word))

        elif word in ['+', '-', '*', '/']:
            bin_op(stack, word)

        elif word == "dup":
            dup(stack)

        elif word == "drop":
            drop(stack)

        elif word == "swap":
            swap(stack)

        elif word == "over":
            over(stack)

        elif word == "rot":
            rot(stack)

        elif word == '.':
            if stack:
                print(stack.pop())
            else:
                print("Stack is empty.")

        elif word == ':':
            i = define_word(words, i + 1)

        elif word in definitions:
            execute(definitions[word])

        else:
            print("Unknown word:", word)

        i += 1

def define_word(words, start_index):
    if start_index >= len(words):
        print("Error: Incomplete word definition.")
        return len(words)

    word_name = words[start_index]
    end_index = start_index + 1

    while end_index < len(words) and words[end_index] != ';':
        end_index += 1

    if end_index == len(words):
        print("Error: Incomplete word definition.")
        return len(words)

    word_definition = ' '.join(words[start_index + 1:end_index])
    definitions[word_name] = word_definition

    return end_index

while True:
    input_str = input("Forth> ")
    if input_str.lower() == 'quit':
        break
    execute(input_str)

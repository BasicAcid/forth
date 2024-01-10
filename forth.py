#! /usr/bin/python3

stack = []
definitions = {}

def execute(input_str):
    words = input_str.split()

    i = 0
    while i < len(words):
        word = words[i]

        if word.isdigit():
            stack.append(int(word))

        # TODO: create func for this block.
        elif word == '+':
            if len(stack) < 2:
                print(f"Error: Not enough op_s for: {word}")
                return
            else:
                op_2 = stack.pop()
                op_1 = stack.pop()
                result = op_1 + op_2
                stack.append(result)
        elif word == '-':
            if len(stack) < 2:
                print(f"Error: Not enough op_s for: {word}")
                return
            else:
                op_2 = stack.pop()
                op_1 = stack.pop()
                result = op_1 - op_2
                stack.append(result)
        elif word == '*':
            if len(stack) < 2:
                print(f"Error: Not enough op_s for: {word}")
                return
            else:
                op_2 = stack.pop()
                op_1 = stack.pop()
                result = op_1 * op_2
                stack.append(result)
        elif word == '/':
            if len(stack) < 2:
                print(f"Error: Not enough op_s for: {word}")
                return
            else:
                op_2 = stack.pop()
                op_1 = stack.pop()
                result = op_1 / op_2
                stack.append(result)

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

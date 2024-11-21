import os
import ast
import datetime

def output(store):

    file = open('README.md', 'w')

    output_str = ""
    
    store = dict(sorted(store.items(), key=lambda item: item[1]))
    store = {k: store[k] for k in reversed(store)}

    for i, item in enumerate(store):
        output_str += f"|{i + 1}.|{list(store)[i]}|{store[item]}|\n"

    log = open('log.txt', 'r')
    lines = log.readlines()
    for i in lines:
        output_str += i + '\n'
    log.close()

    file.write(output_str)
    file.close()
    
def save(store):
    file = open('store.txt', 'w')

    file.write(str(store))

    file.close()

store = open('store.txt', 'r')

scores = ast.literal_eval(store.read())

while True:

    for i in scores:
        print(i, ":", scores[i])

    options = ("post", "delete", "exit")
    while True:
        choice = input(f"Input operation {options}: ")
        if choice in options:
            break
        print("Enter valid option.")

    if choice == "exit":
        break
    elif choice == "delete":

        while True:
            remove_choice = input("Input person to remove: ")
            if remove_choice in scores:
                break
            print("Enter Valid option.")

        scores.pop(remove_choice)
        
        send_to_log(f'{datetime.datetime.now()} \| Remove \| {remove_choice}')

    elif choice == "post":

        while True:
            name = input("Input name to add: ")
            if name not in scores:
                break
            print("Person already exists.")
        
        scores[name] = 0
        send_to_log(f'{datetime.datetime.now()} \| Add \| {name}')
    os.system("cls")

output(scores)
save(scores)

store.close()
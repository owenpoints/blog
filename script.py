import os
import ast
import datetime

def output(store):

    file = open('README.md', 'w')

    output_str = ""
    
    for i, item in enumerate(store):
        output_str += f"{store[item]}\n\n"

    file.write(output_str)
    file.close()
    
def save(store):
    file = open('store.txt', 'w')

    file.write(str(store))

    file.close()

store = open('store.txt', 'r')

posts = ast.literal_eval(store.read())

while True:

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
            remove_choice = input("Input post to remove: ")
            if remove_choice in posts:
                break
            print("Enter Valid option.")

        posts.pop(remove_choice)
        

    elif choice == "post":
        posts[len(posts) + 1] =  str(datetime.datetime.now()) + ": " + input("Input post contents: ")
        
    os.system("cls")

output(posts)
save(posts)

store.close()
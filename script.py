import os
import ast
import datetime

user = open('username.txt', 'r')
username = user.read()
user.close()

def show_posts(store):
    for i in store:
        print(f'{i}: {store[i].split("::")[1]}')

def output(store):

    os.system("del posts\*.md")



    file = open('README.md', 'w')

    output_str = "# Top Owen Updates\n"
    
    for i, item in enumerate(store):
        output_str += f'{store[item].split("::")[0]} [{item}](./posts/{i}.md)\n\n'

        temp = open(f'posts\{i}.md', 'w')
        temp.write(f'{store[item]} \n\n Click [Here](../) to Go Back')
        temp.close()
        




    file.write(output_str)
    file.close()
    
def save(store):
    file = open('store.txt', 'w')

    file.write(str(store))

    file.close()

store = open('store.txt', 'r')

posts = ast.literal_eval(store.read())

while True:

    options = ("post", "delete", "list", "exit")
    while True:
        choice = input(f"Input operation {options}: ")
        if choice in options:
            break
        print("Enter valid option.")

    if choice == "exit":
        break
    elif choice == "delete":
        
        show_posts(posts)

        while True:
            remove_choice = int(input("Input post to remove: "))
            if remove_choice in posts:
                break
            print("Enter Valid option.")

        posts.pop(remove_choice)

        temp = {}
        for i, item in enumerate(posts):
            temp[i] = posts[item]
        
        posts = temp

    elif choice == "post":

        while True:
            title = input("Input title of post: ")
            if title not in posts:
                break
            print("That title already exists.")

        while True:
            contents = input("Input post contents: ")
            if not "::" in contents:
                break
            print("Post cannot contain '::'.")

        posts[title] =  f'{datetime.datetime.now()} \| {username}:: {contents}'
    
    elif choice == "list":
        show_posts(posts)
        os.system("pause")
        
    os.system("cls")

output(posts)
save(posts)

store.close()
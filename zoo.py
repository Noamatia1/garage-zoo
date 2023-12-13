import json
import os
from helper import menu2

zoo =[]
MY_DATA='zoo.txt'

def load_data():
    global zoo
    with open(MY_DATA, 'r') as filehandle:
        zoo = json.load(filehandle)

def save_2_file():
    with open(MY_DATA, 'w') as filehandle:
        json.dump(zoo, filehandle)

def do_menu_actions(userSelection):
    if userSelection == 'x': # when closing the applicaion
        save_2_file()
        print("bye bye")
        exit()
    if userSelection == 'p': print(zoo)
    if userSelection == 'a': zoo.append({"species":input("animal species?"),"age":input("animal age?"),"gender":input("gender?")})
    if userSelection == 'd': print("not implemented yet - premium version only")

def main():
    load_data()
    while(True):
        menu2()
        userSelection = input("please select action")
        os.system('cls' if os.name == 'nt' else 'clear') #clear terminal
        do_menu_actions(userSelection)

if __name__ == "__main__":
    main()
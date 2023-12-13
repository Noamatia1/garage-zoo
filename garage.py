import json
import os
from helper import menu

cars =[]
MY_DATA='garage.txt'

def load_data():
    global cars
    with open(MY_DATA, 'r') as filehandle:
        cars = json.load(filehandle)

def save_2_file():
    with open(MY_DATA, 'w') as filehandle:
        json.dump(cars, filehandle)

def do_menu_actions(userSelection):
    if userSelection == 'x': # when closing the applicaion
        save_2_file()
        print("bye bye")
        exit()
    if userSelection == 'p': print(cars)
    if userSelection == 'a': cars.append({"model":input("car model?"),"color":input("car color?"),"brand":input("car brand?")})
    if userSelection == 'd': print("not implemented yet - premium version only")

def main():
    load_data()
    while(True):
        menu()
        userSelection = input("please select action")
        os.system('cls' if os.name == 'nt' else 'clear') #clear terminal
        do_menu_actions(userSelection)

if __name__ == "__main__":
    main()
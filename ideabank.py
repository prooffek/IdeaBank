# Put your code here
import signal
import os
from pathlib import Path
import csv

def new_idea(list_of_ideas):
    os.system("cls | clear")
    while True:
        try: 
            user_input = input("What is your new idea? ")
            list_of_ideas.append(user_input)
            actual_list(list_of_ideas)
        except KeyboardInterrupt:
            print_list(list_of_ideas)
            if return_to_menu("return to main manu"):
                main()
            else:
                print("See you later, mate!")
                exit()

def print_list(list_of_ideas):
    os.system("cls | clear")
    
    n = 0
    for element in list_of_ideas:
        n += 1
        print(f"{n}. {element}")

def remove_idea(list_of_ideas):
    user_input = False
    while user_input is False:
        os.system("cls | clear")
        print_list(list_of_ideas)
        user_input = input("Which idea you want to remove? (Give its number): ")
        if user_input.lower() == "quit":
            main()
        else:
            try:
                number = int(user_input)
                if number > len(list_of_ideas):
                    print("Number out of range.", end = " ")
                    user_input = False
                else:
                    os.system("cls | clear")
                    print(f"'{list_of_ideas[number - 1]}' has been removed.")
                    del list_of_ideas[number - 1]
                    actual_list(list_of_ideas)
                    if return_to_menu("remove another idea"):
                        user_input = False
                    else:
                        main()
            except ValueError:
                print("Wrong input.", end = " ")
                user_input = False

def get_list():
    list_of_ideas = []

    path = Path(__file__).parent
    file_name = f"{path}/list_of_ideas.csv"
    
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            for element in row:
                list_of_ideas.append(element)

    return list_of_ideas

def actual_list(list_of_ideas):
    path = Path(__file__).parent
    file_name = f"{path}/list_of_ideas.csv"

    file_name = open(file_name, "w")
    csv_writer = csv.writer(file_name)
    csv_writer.writerow(list_of_ideas)
    file_name.close()

def return_to_menu(word):
    user_input = False
    while user_input is False:
        user_input = input(f"Do you want to {word}? (y/n) ")
        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        else:
            user_input = False

def main_menu():
    user_input = input("What do you want to do?\n\n\t1. Add a new idea.\n\t2. See the list of ideas.\n\t3. remove an idea.\n\t4. Quit.\n\n")

    while user_input not in ["1", "2", "3", "4"]:
        print("Command does not exist.", end=" ")
        user_input = input("What do you want to do?\n\n\t1. Add a new idea.\n\t2. See the list of ideas.\n\t3. remove an idea.\n\t4. Quit.\n\n")

    return user_input

def main():
    os.system("cls | clear")
    user_input = main_menu()
    list_of_ideas = get_list()

    if user_input == "1":
        new_idea(list_of_ideas)
    elif user_input == "2":
        print_list(list_of_ideas)
        if return_to_menu("return to main manu"):
            main()
        else:
            print("See you later, mate!")
            exit()
    elif user_input == "3":
        remove_idea(list_of_ideas)
    else:
        os.system("cls | clear")
        print("See you later, mate")
        exit()


main()
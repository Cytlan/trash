"""
Some dumbass program
Name: Dick Tracy
Date started: Yesterday
Github URL: No
"""
import csv # "you're not expected to use the csv module, but you're welcome to" - Don't mind if I do!

def print_menu():
    print("""Menu:
L - List places
R - Recommend random place
A - Add new place
M - Mark a place as visited
Q - Quit""")

def read_places(filename):
    places = []
    with open(filename, newline='') as csvfile:
        placesReader = csv.reader(csvfile)
        for row in placesReader:
            places.append(row)
    return places

def main():
    print("Travel Tracker 1.0 - by Go Away")

    # Read the list of places and parse it
    places = read_places("places.csv")
    print(places)

    # I will use the CORRECT method of implementing a menu
    # The way you've been taught how to implement a CLI menu is amature hour stuff
    while True:
        print_menu()
        selection = input(">>> ").upper()
        if selection == "L":
            pass
        elif selection == "R":
            pass
        elif selection == "A":
            pass
        elif selection == "M":
            pass
        elif selection == "Q":
            break
        else:
            print("Invalid menu choice")

if __name__ != "__main__":
    pass
else:
    main()

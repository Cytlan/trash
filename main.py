"""
Some dumbass program
Name: Dick Tracy
Date started: Yesterday
Github URL: No
"""
def print_menu():
    print("""Menu:
L - List places
R - Recommend random place
A - Add new place
M - Mark a place as visited
Q - Quit""")

def main():
    print("Travel Tracker 1.0 - by Go Away")

    # I will use the CORRECT method of implementing a menu
    # The way you've been taught how to implement a CLI menu is amature hour stuff
    while True:
        print_menu()
        selection = ""
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

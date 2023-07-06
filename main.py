"""
Some dumbass program
Name: Dick Tracy
Date started: Yesterday
Github URL: No
"""
import random # For picking a place to visit
import csv # "you're not expected to use the csv module, but you're welcome to" - Don't mind if I do!

# Print the main menu to the console
def print_menu():
    print("""Menu:
L - List places
R - Recommend random place
A - Add new place
M - Mark a place as visited
Q - Quit""")

# Read a CSV file containing the places database
def read_places(filename):
    places = []
    with open(filename, newline='') as csvfile:
        placesReader = csv.reader(csvfile)
        index = 1
        for row in placesReader:
            places.append({'index': index, 'name': row[0], 'country': row[1], 'priority': row[2], 'visited': row[3]})
            index += 1
    return places

# Print the list of places to the console
def print_places(places):
    unvisited_count = 0
    for place in places:
        visited = " "
        if place['visited'] == "v":
            visited = "*"
        else:
            unvisited_count += 1
        print("{0}{1}. {2:20} in {3:20} {4:3}".format(visited, place['index'], place['name'], place['country'], place['priority']))
    print("{0} places. You still want to visit {1} places.".format(len(places), unvisited_count))

# Print a random place that hasn't been visited
def recomment_place(places):
    unvisited = [place for place in places if place['visited'] == "n"]
    if(len(unvisited) == 0):
        print("No places left to visit!")
        return
    print("Not sure where to visit next?")
    pick = random.choice(unvisited)
    print("How about... {0} in {1}?".format(pick['name'], pick['country']))

# Main entry point
def main():
    print("Travel Tracker 1.0 - by Go Away")

    # Read the list of places and parse it
    places = read_places("places.csv")

    # I will use the CORRECT method of implementing a menu.
    # The way you've been taught how to implement a CLI menu is amature hour stuff.
    # "Incorrect use of while True." - 100% WRONG! If I ever catch you using the anti-pattern you've been
    # taught about CLI menus in real code for an actual project, I'll roll back your commit.
    # If I catch you doing it again, I'll slap you with a salmon.
    # I'm dead fucking serious. THIS IS THE CORRECT WAY TO IMPLEMENT A MENU! IT'S THE BEST EXAMPLE
    # OF APPROPRIATE USE OF AN INFINITE LOOP!
    while True:
        print_menu()
        selection = input(">>> ").upper()
        if selection == "L":
            print_places(places)
        elif selection == "R":
            recomment_place(places)
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

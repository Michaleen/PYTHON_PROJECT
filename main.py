# import our modules
from read_films import read_film
from add_films import add_film
from update_films import update_film
from delete_films import delete_film
from filter_films import filter_film

# create menu functionality
def menuOptions():
    options = 0
    while options not in ["1", "2", "3", "4", "5","6"]:
        print(
            """
            Main Menu Options 
            
            1. Display all Films
            2. Add Films to database
            3. Update Films
            4. Delete Films
            5. Filter Films
            6. Exit the Application
        """)
        options = input("Enter a number from the above Options: ")
        if options not in ["1", "2", "3", "4", "5", "6"]:
            print(options + " is not within the above options. Please enter a number between (1-6).")
    return options


mainProgram = True # "flag" variable
while mainProgram:
    mainMenu = menuOptions()
    if mainMenu == "1":
        read_film()
    elif mainMenu == "2":
        add_film()
    elif mainMenu == "3":
        update_film()
    elif mainMenu == "4":
        delete_film()
    elif mainMenu == "5":
        filter_film()
    else:
        mainProgram =False

input("Press Enter to exit: ")

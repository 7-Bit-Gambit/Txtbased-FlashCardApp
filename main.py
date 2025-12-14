from check_knowledge_level import check_knowledge_level
from create_deck import create_deck
from learn_from_deck import learn_from_deck
from edit_deck import edit_deck


def main_menu():
    #Insert a check if files are available -> if no then...
    while True:
        print("what would you like to do today?")
        print("1. Learn from a deck.")
        print("2. Create a deck.")
        print("3. Edit or delete a deck.")
        print("4. Check your knowledge level.")
        print("(To terminate the app press enter)")
        selection = input("Enter your choice: ")

        # load deck selection
        if selection == "1":
            learn_from_deck()

        # load deck creator
        elif selection == "2":
            create_deck()

        # load deck deleter
        elif selection == "3":
            edit_deck()

        # load level calculator
        elif selection == "4":
            check_knowledge_level()


        elif selection:
            print ("Undefined selection. \nSelect a number from 1 - 4 to continue. \n")
        else:
            print("goodbye, thank you for using our flashcard application!")
            break

if __name__ == "__main__":
    print("Hello!")
    print("Welcome to your Console Based Flashcard-App")
    main_menu()

### 22:08###


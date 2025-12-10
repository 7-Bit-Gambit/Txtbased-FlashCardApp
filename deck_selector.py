from config import list_deck_paths

def choose_deck_helper():
    while True:
        decks = list_deck_paths()
        if not decks:
            print("No decks found.")
            return None

        print("Available decks:")
        for i, d in enumerate(decks, start=1):
            print(f"{i}. {d.stem}")

        selection = input("Choose a deck number (to leave this menu leave the input empty): ").strip()

        if selection == "":
            return None

        if not selection.isdigit():
            print("Invalid selection.")
            continue

        n = int(selection)
        if not 1 <= n <= len(decks):
            print("Selection out of range.")
            continue

        return decks[n - 1]



from card_helpers import add_cards_loop
from config import DECK_DIRECTORY
from deck_helpers import save_deck

def create_deck():
    raw_name = input("Name your deck: ").strip().lower()
    if not raw_name:
        print("Deck creation cancelled.")
        return

    deck_path = DECK_DIRECTORY / f"{raw_name}.csv"

    # prevent overwriting existing deck
    if deck_path.exists():
        overwrite = input(
            "A deck with that name already exists. Overwrite? Enter: Y to overwrite, enter to continue: "
        ).strip().lower()
        if overwrite != "y":
            print("Cancelled. Keeping existing deck.")
            return

    print(f"Deck {raw_name} created.")

    a = input("Would you like to populate the deck? Enter 'Y' to continue: ").strip().lower()

    cards = []
    #counter = 0

    if a == "y":
        add_cards_loop(cards)
        #counter += 1

        print("Deck creation complete. You added", len(cards), "cards to your deck.") #, counter
    else:
        print("Created empty deck.")

    #  always write at least header (and cards, if any)
    save_deck(deck_path, cards)

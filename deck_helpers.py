import csv
from config import HEADERS
from config import list_deck_paths

def read_deck(deck_path):
    with open(deck_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        cards = [
            row for row in reader
            if row.get("question")
               and row.get("answer")
               and row.get("level")
        ]
        return cards

def save_deck(deck_path, cards):
    """Write the deck (with header) to CSV.

    cards must be a list of dicts with keys in HEADERS.
    """
    with deck_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writeheader()
        for card in cards:
            writer.writerow({
                "question": card["question"],
                "answer": card["answer"],
                "level": card["level"],
            })

def choose_deck_helper():
    while True:
        decks = list(list_deck_paths())

        if not decks:
            print("No decks found.")
            return None

        print("These are the available decks:")
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

def delete_deck():
    deck = choose_deck_helper()
    if deck is None:
        return

    print("Deleting a deck... ", deck.stem)
    deck.unlink()








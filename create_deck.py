import csv  # still needed if you use csv elsewhere
from config import DECK_DIRECTORY
from datahandlers import save_deck

def create_deck():
    raw_name = input("Name your deck: ").strip().lower()
    if not raw_name:
        print("Deck creation cancelled.")
        return

    deck_path = DECK_DIRECTORY / f"{raw_name}.csv"

    # prevent overwriting existing deck
    if deck_path.exists():
        overwrite = input(
            "A deck with that name already exists. Overwrite? (Y/N): "
        ).strip().lower()
        if overwrite != "y":
            print("Cancelled. Keeping existing deck.")
            return

    print(f"Deck {raw_name} created.")

    a = input("Would you like to populate the deck? (Y/N): ").strip().lower()

    cards = []
    counter = 0

    if a == "y":
        print("Fill out the questions and answers for your deck. "
              "Leave the question empty to finish.")
        while True:
            question = input("Question: ").strip()
            if question == "":
                break

            answer = input("Answer: ").strip()
            if answer == "":
                print("Answer cannot be empty, card skipped.")
                continue

            cards.append({
                "question": question,
                "answer": answer,
                "level": "0",
            })
            counter += 1

        print("Deck creation complete. You added", counter, "cards to your deck.")
    else:
        print("Created empty deck.")

    #  always write at least header (and cards, if any)
    save_deck(deck_path, cards)

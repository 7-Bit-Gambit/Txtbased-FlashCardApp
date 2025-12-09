import csv
from config import DECK_DIRECTORY, HEADERS

def create_deck():
    """create a new deck file"""
    raw_name=input("Name your deck:").strip()
    if not raw_name:
        print("Deck creation cancelled.")
        return
    deck_path = DECK_DIRECTORY / f"{raw_name}.csv"

    #prevent overwriting existing deck
    if deck_path.exists():
        overwrite = input("A deck with that name already exists. Overwrite? (Y/N): ").strip().lower()
        if overwrite != "y":
            print("Cancelled. Keeping existing deck.")
            return

    with deck_path.open("w",newline="",encoding="utf-8")as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)
            print(f"Deck {raw_name} created.")

            a = (input("would you like to populate the deck? Y/N")).lower()
            if a == "y":
                counter = 0
                print("Fill out the questions and answers for your deck. Leave the question empty to finish")
                while True:
                    question = input("Question: ").strip()
                    if question == "":
                        break
                    answer = input("Answer: ").strip()
                    if answer == "":
                        print("Answer cannot be empty, card skipped.")
                        continue
                    writer.writerow([question,answer,0])
                    counter += 1
                print("Deck creation complete. You added ", counter, "cards to your deck.")

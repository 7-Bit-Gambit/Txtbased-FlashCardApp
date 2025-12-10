import csv
from config import DECK_DIRECTORY, HEADERS
from deck_selector import choose_deck_helper
from datahandlers import save_deck

def learn_from_deck():
    deck_path = choose_deck_helper()
    if deck_path is None:
        print("No deck selected. Returning to main menu.")
        return

    print(f"\nOpening deck: {deck_path.stem}")

    #read deck
    with open(deck_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        cards = [row for row in reader if row["question"] and row["answer"] and row ["level"]]
        correct = 0

        for i, card in enumerate(cards, start=1):
            print(f"\n[{i}/{len(cards)}] Q: {card['question']}")
            a = input("What's the answer? ")

            if a == card["answer"]:
                correct += 1
                print(f"Correct!")
                card["level"] = str((int(card["level"]) + 1))

            elif a == "":
                print("learning session has been terminated")
                break

            else:
                print(f"Wrong! the answer is {card['answer']}")
                # I want to decrease the Level in the row
                card["level"] = str((int(card["level"]) - 1))
    #save progress after the session
    save_deck(deck_path, cards)

    print("Progress saved.")
    print(f"You got {correct} out of {len(cards)} correct!")
    print("Returning to main menu")

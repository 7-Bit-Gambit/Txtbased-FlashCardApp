import csv
from config import DECK_DIRECTORY, HEADERS

def learn_from_deck():
    decks = sorted(file.stem for file in DECK_DIRECTORY.glob("*.csv"))
    if not decks:
        print("No decks found. Please create one first.")
        return
    print("These are the available decks:", decks)
    name = input("Enter the deck you would like to open: ").strip().lower()
    deck_path = DECK_DIRECTORY / f"{name}.csv"
    if not deck_path.exists():
        print("Deck not found.")
        return
    
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
    with open(deck_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writeheader()
        for c in cards:

            # ensure only known columns are written
            writer.writerow({
                "question": c["question"],
                "answer": c["answer"],
                "level": c["level"],
            })

    print("Progress saved.")
    print(f"You got {correct} out of {len(cards)} correct!")
    print("Returning to main menu")

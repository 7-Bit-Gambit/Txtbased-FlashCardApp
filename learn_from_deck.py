from deck_selector import choose_deck_helper
from datahandlers import save_deck, read_deck
import random

def learn_from_deck():
    deck_path = choose_deck_helper()
    if deck_path is None:
        print("No deck selected. Returning to main menu.")
        return

    print(f"\nOpening deck: {deck_path.stem}")

    cards = read_deck(deck_path)
    correct = 0

    random.shuffle(cards)

    for i, card in enumerate(cards, start=1):
        print(f"\n[{i}/{len(cards)}] Q: {card['question']}")
        a = input("What's the answer? ").strip()

        if a == "":
            print("Learning session has been terminated.")
            break

        if a == card["answer"]:
            correct += 1
            print("Correct!")
            card["level"] = str(min(int(card["level"]) + 1, 5))
        else:
            print(f"Wrong! the answer is {card['answer']}")
            # decrease down to -5
            card["level"] = str(max(int(card["level"]) - 1, -5))

    save_deck(deck_path, cards)

    print("Progress saved.")
    print(f"You got {correct} correct (session).")
    print("Returning to main menu")

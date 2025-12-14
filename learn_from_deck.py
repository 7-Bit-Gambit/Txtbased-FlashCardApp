from deck_selector import choose_deck_helper
from deck_helpers import read_deck, save_deck
import random

def learn_from_deck():
    deck_path = choose_deck_helper()
    if deck_path is None:
        print("No deck selected. Returning to main menu.")
        return

    print(f"\nOpening deck: {deck_path.stem}")

    cards = read_deck(deck_path)

    # filter only for this session
    learn_cards = [c for c in cards if int(c["level"]) < 5]

    if not learn_cards:
        print("All cards are already at level 5. Nothing to learn 🎉")
        return

    random.shuffle(learn_cards)
    correct = 0

    for i, card in enumerate(learn_cards, start=1):
        print(f"\n[{i}/{len(learn_cards)}] Q: {card['question']}")
        a = input("What's the answer? ").strip()

        if a == "":
            print("Learning session terminated.")
            break

        if a == card["answer"]:
            correct += 1
            print("Correct!")
            card["level"] = str(min(int(card["level"]) + 1, 5))
        else:
            print(f"Wrong! The answer is {card['answer']}")
            card["level"] = str(max(int(card["level"]) - 1, -5))

    save_deck(deck_path, cards)

    print("Progress saved.")
    print(f"You got {correct} correct this session.")
    print("Returning to main menu.")
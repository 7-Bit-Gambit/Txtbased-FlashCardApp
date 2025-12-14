import csv
from config import DECK_DIRECTORY
from deck_helpers import read_deck

def check_knowledge_level():
        print("this is your level for each deck")
        decks = sorted(DECK_DIRECTORY.glob("*.csv"))

        if not decks:
            print("No decks found.")
        else:
            for deck_path in decks:
                cards = read_deck(deck_path)

                levels = [int(card["level"]) for card in cards]

                if levels:
                    avg = sum(levels) / len(levels)
                    print(f"{deck_path.stem}: average level {avg:.2f}  ({len(levels)} cards)")
                else:
                    print(f"{deck_path.stem}: no valid level data")

        input("\nPress Enter to continue...")
import csv
from config import DECK_DIRECTORY

def check_knowledge_level():
        print("this is your level for each deck")
        decks = sorted(DECK_DIRECTORY.glob("*.csv"))

        if not decks:
            print("No decks found.")
        else:
            for deck_path in decks:
                with deck_path.open("r", newline="", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    levels = []
                    for row in reader:
                        if row.get("level") and row.get("level"):
                            levels.append(int(row["level"]))

                    if levels:
                        avg = sum(levels) / len(levels)
                        print(f"{deck_path.stem}: average level {avg:.2f}  ({len(levels)} cards)")
                    else:
                        print(f"{deck_path.stem}: no valid level data")

        input("\nPress Enter to continue...")
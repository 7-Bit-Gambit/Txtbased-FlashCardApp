from config import DECK_DIRECTORY

def check_knowledge_level():
    """check the knowledge/score for the selected deck"""
    print("this is your level")
    decks = sorted(DECK_DIRECTORY.glob("*.csv"))
    #if deck does not exist
    if not decks:
        print("No decks found.")
        return
    for deck_path in decks:
        with deck_path.open("r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            levels = []
            for row in reader:
                if row.get("level") and row.get("level").isdigit():
                    levels.append(int(row["level"]))

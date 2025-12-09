from config import DECK_DIRECTORY

def delete_deck():
    """delete an existing deck file"""
    decks = sorted(file.stem for file in DECK_DIRECTORY.glob("*.csv"))
    print("These are the available decks:", decks)
    raw_name = input("What deck do you want to delete?").strip().lower()
    file_path = DECK_DIRECTORY / f"{raw_name}.csv"
    if file_path.exists():
        file_path.unlink()
        print("File deleted.")
    else:
        print("File not found.")

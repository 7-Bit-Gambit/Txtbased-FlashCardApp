from pathlib import Path

DECK_DIRECTORY = Path("decks")
DECK_DIRECTORY.mkdir(exist_ok=True)

HEADERS = ["question", "answer", "level"]

def list_deck_paths():
    """Return a sorted list of deck Path objects."""
    return sorted(DECK_DIRECTORY.glob("*.csv"))

def list_deck_names():
    """Return a sorted list of deck names (without .csv)."""
    return [p.stem for p in list_deck_paths()]
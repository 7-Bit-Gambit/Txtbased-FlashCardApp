import csv
from config import HEADERS

def read_deck(deck_path):
    with open(deck_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        cards = [
            row for row in reader
            if row.get("question")
               and row.get("answer")
               and row.get("level")
               and int(row["level"]) < 5  # <-- NEW: ignore maxed-out cards
        ]
        return cards

def save_deck(deck_path, cards):
    """Write the deck (with header) to CSV.

    cards must be a list of dicts with keys in HEADERS.
    """
    with deck_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writeheader()
        for card in cards:
            writer.writerow({
                "question": card["question"],
                "answer": card["answer"],
                "level": card["level"],
            })
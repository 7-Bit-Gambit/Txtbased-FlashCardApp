"""
Functions regarding deck handling (CSV handlers)
"""
from card_helpers import add_cards_loop
from deck_helpers import read_deck, save_deck, choose_deck_helper, delete_deck

def _print_cards(cards, max_len=60):
    if not cards:
        print("\n(No cards in this deck yet.)\n")
        return

    print("\nCards:")
    for i, c in enumerate(cards, start=1):
        q = c["question"]
        a = c["answer"]
        if len(q) > max_len:
            q = q[:max_len - 1] + "…"
        if len(a) > max_len:
            a = a[:max_len - 1] + "…"
        print(f"{i:>3}. Q: {q} | A: {a}")
    print()

def _select_card_index(cards, prompt):
    """Return index (0-based) or None if cancelled/invalid."""
    if not cards:
        print("No cards available.")
        return None

    raw = input(prompt).strip()
    if raw == "":
        return None
    if not raw.isdigit():
        print("Please enter a valid number.")
        return None

    idx = int(raw) - 1
    if idx < 0 or idx >= len(cards):
        print("Number out of range.")
        return None
    return idx

def _edit_cards_loop(cards):
    """List -> pick -> edit -> list again until user exits."""
    if not cards:
        print("No cards to edit.")
        return False

    changed = False
    while True:
        _print_cards(cards)
        idx = _select_card_index(cards, "Edit which card number? (Enter to exit): ")
        if idx is None:
            print("Number is out of range. Returning to menu.")
            break

        card = cards[idx]
        print("\nLeave empty to keep current value.")
        print(f"Current question: {card['question']}")
        new_q = input("New question: ").strip()
        if new_q:
            card["question"] = new_q

        print(f"Current answer:   {card['answer']}")
        new_a = input("New answer: ").strip()
        if new_a:
            card["answer"] = new_a

        print("Card updated.")
        changed = True

    return changed

def _remove_cards_loop(cards):
    """List -> pick -> confirm delete -> list again until user exits."""
    if not cards:
        print("No cards to remove.")
        return False

    changed = False
    while True:
        _print_cards(cards)
        idx = _select_card_index(cards, "Remove which card number? (Enter to exit): ")
        if idx is None:
            break

        card = cards[idx]
        confirm = input(f"Delete card {idx+1}? Type Y to confirm, or enter to cancel: ").strip().lower()
        if confirm == "y":
            cards.pop(idx)
            print("Card removed.")
            changed = True
        else:
            print("Delete cancelled.")

        if not cards:
            print("Deck is now empty.")
            break

    return changed

def edit_deck():
    deck_path = choose_deck_helper()
    if deck_path is None:
        print("No deck selected.")
        return

    cards = read_deck(deck_path)

    while True:
        print(f"\nDeck editor: {deck_path.stem}")
        print("1. Add card")
        print("2. Edit cards (use to view cards in deck)")
        print("3. Remove cards")
        print("4. Delete whole deck")  # optional
        print("(Press Enter to exit)")

        choice = input("Choose: ").strip()

        if choice == "":
            break

        elif choice == "1":
            if add_cards_loop(cards):
                save_deck(deck_path, cards)

        elif choice == "2":
            if _edit_cards_loop(cards):
                save_deck(deck_path, cards)

        elif choice == "3":
            if _remove_cards_loop(cards):
                save_deck(deck_path, cards)

        elif choice == "4":
            confirm = input(f"Type Y to permanently delete, or enter to cancel '{deck_path.stem}': ").strip().lower()
            if confirm == "y":
                delete_deck(deck_path)
                print("Deck deleted.")
                return
            else:
                print("Delete cancelled.")

        else:
            print("Invalid choice.")
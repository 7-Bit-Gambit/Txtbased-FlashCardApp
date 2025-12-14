def ui_new_card(default_level="0"):
    """
    Ask the user for a new flashcard.
    Returns a dict {"question","answer","level"} or None if cancelled.
    """
    q = input("Question (Enter to cancel): ").strip()
    if q == "":
        return None

    a = input("Answer: ").strip()
    if a == "":
        print("Answer cannot be empty. Cancelled.")
        return None

    return {"question": q, "answer": a, "level": str(default_level)}


def add_cards_loop(cards, default_level="0"):
    """
    Repeatedly ask for cards and append them.
    Returns True if at least one card was added.
    """
    added_any = False
    print("\nAdd cards (press Enter at question to stop)\n")

    while True:
        card = ui_new_card(default_level=default_level)
        if card is None:
            break
        cards.append(card)
        added_any = True
        print("Card added.\n")

    return added_any
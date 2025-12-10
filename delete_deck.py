from deck_selector import choose_deck_helper

def delete_deck():
    deck = choose_deck_helper()
    if deck is None:
        return

    deck.unlink()




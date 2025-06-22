# Number of cards arranged in decreasing order, have to pick one specific card from the ordered cards such that the number of moves involved is minimum.

# Brute Force -> Liear Search. O(n)
# Worst case scenario, had to flip all cards one by one.
cards = []

def locate_cards_linear(cards, query):
    position:0 #keeps the track of the card number
    if (len(cards) < 0):
        print("Invalid Card Deck")
    else:
        while (len(cards)>position):
            if cards[position] == query:
                return position
            position+=1
        return -1 #query or the card not found then return -1
# Number of cards arranged in decreasing order, have to pick one specific card from the ordered cards such that the number of moves involved is minimum.

# Optimal Solution -> Binary Search. O(log n)
cards=[]
def locate_card_binary(cards, query):
    low = 0
    high = len(cards)-1
    
    while (high>=low):
        mid = (high-low)//2
        mid_number = cards[mid]
        
        if (mid_number==query):
            return mid
        elif (mid_number<query):
            high = mid -1
        elif (mid_number>query):
            low = mid +1
    return -1 
    
  
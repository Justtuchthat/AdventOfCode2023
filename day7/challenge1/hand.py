from enum import Enum

handVals = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

class Hand:
    def __init__(self, line):
        hands = line.split(' ')
        self.hand = hands[0]
        self.bet = int(hands[1])
        self.type = HandType.getHandType(self.hand)
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.hand == other.hand
        return False
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        if isinstance(other, self.__class__):
            if self.type != other.type:
                return self.type < other.type
            for a, b in zip(self.hand, other.hand):
                if handVals[a] != handVals[b]:
                    return handVals[a] < handVals[b]
        return False
    
    def __le__(self, other):
        if isinstance(other, self.__class__):
            if self == other:
                return True
            return self < other
        return False
    
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            if self <= other:
                return False
            return True
        return False
    
    def __ge__(self, other):
        if isinstance(other, self.__class__):
            if self == other:
                return True
            return self > other
        return False
    
    def __repr__(self):
        string = "Hand " + self.hand + " with a bet of " + str(self.bet)
        string += " is of the type " + str(self.type)
        return string


class HandType(Enum):
    HIGHCARD = 1
    ONEPAIR = 2
    TWOPAIR = 3
    THREEOFAKIND = 4
    FULLHOUSE = 5
    FOUROFAKIND = 6
    FIVEOFAKIND = 7

    def getHandType(hand):
        dct = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, 'T': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0}
        for let in hand:
            dct[let] += 1
        cards = sorted(dct.values())
        if cards[-1] == 5:
            return HandType.FIVEOFAKIND
        if cards[-1] == 4:
            return HandType.FOUROFAKIND
        if cards[-1] == 3:
            if cards[-2] == 2:
                return HandType.FULLHOUSE
            return HandType.THREEOFAKIND
        if cards[-1] == 2:
            if cards[-2] == 2:
                return HandType.TWOPAIR
            return HandType.ONEPAIR
        return HandType.HIGHCARD

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.value == other.value
        return False
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.value < other.value
        return False
    
    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self.value <= other.value
        return False
    
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.value > other.value
        return False
    
    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return self.value >= other.value
        return False
    
    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        match self:
            case HandType.HIGHCARD:
                return "High card"
            case HandType.ONEPAIR:
                return "One pair"
            case HandType.TWOPAIR:
                return "Two pair"
            case HandType.THREEOFAKIND:
                return "Three of a kind"
            case HandType.FULLHOUSE:
                return "Full house"
            case HandType.FOUROFAKIND:
                return "Four of a kind"
            case HandType.FIVEOFAKIND:
                return "Five of a kind"
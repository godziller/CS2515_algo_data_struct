""" Class definitions for implementing a playing card, for use in games.

    Test functions use the command line for interaction.
"""

class Card:
    """A standard playing card. """

    def __init__(self, rank, suit):
        """ Initialise the card.

            rank should be an integer in {1,2,...,13}
            suit should be an integer in {1,2,3,4}

        """
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return '' + self.name_rank() + self.name_suit()

    def name_rank(self):
        """ Return a string representation of the rank. """
        if self.rank == 1:
            return 'A'
        elif self.rank == 11:
            return 'J'
        elif self.rank == 12:
            return 'Q'
        elif self.rank == 13:
            return 'K'
        else:
            return '' + str(self.rank)

    def name_suit(self):
        """ Return a string representation of the suit. """
        if self.suit == 1:
            return 'S'
        elif self.suit == 2:
            return 'H'
        elif self.suit == 3:
            return 'D'
        else:
            return 'C'

    def is_equal(self, card):
        """ Determine whether this instance is the same card as another. """
        if self.rank == card.rank and self.suit == card.suit:
            return True
        return False

    def is_higher(self, other):
        """ Determine whether this card is higher than another. """
        if self.rank > other.rank:
            return True
        return False
        
    def is_lower(self, other):
        """ Determine whether this card is lower than another. """
        if self.rank < other.rank:
            return True
        return False
        

def lecture_test():
    """ Test the Card class, from lecture. """
    
    c1 = Card(3,4)
    c2 = Card(8,2)
    c3 = Card(8,2)

    print(c1.rank)
    print(c2.suit)
    print(c3)

    if c2.is_equal(c3):
        print('Yes, c2 and c3 represent the same card (but they are different objects)')
    else:
        print('No, c2 and c3 are not the same card (and they are different objects)')
    
if __name__ == "__main__":
    print("Lecture test")
    lecture_test()

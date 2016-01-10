class Poker(object):
    SUITE_ORDER = {'S':4, 'H':3, 'C':2, 'D':1}
    RANK_ORDER = {'GR':15, 'GB':14, 'A':13, 'K':12, 'Q':11, 'J':10, '10':9,
                  '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}
    @classmethod
    def fresh_deck(cls):
        cards = ['AS', 'AH', 'AC', 'AD', '2S', '2H', '2C', '2D', '3S', '3H', '3C', '3D',
                 '4S', '4H', '4C', '4D', '5S', '5H', '5C', '5D', '6S', '6H', '6C', '6D',
                 '7S', '7H', '7C', '7D', '8S', '8H', '8C', '8D', '9S', '9H', '9C', '9D',
                 '10S', '10H', '10C', '10D', 'JS', 'JH', 'JC', 'JD', 'QS', 'QH', 'QC', 'QD',
                 'KS', 'KH', 'KC', 'KD','GR','GB']
        deck = [Card(c) for c in cards]
        return deck


class Card(object):
    def __init__(self, c):
        if not isinstance(c, str):
            raise TypeError("Card must be a str.")

        if len(c) < 2:
            raise ValueError("Invalid card: {0}".format(c))

        c = c.upper()
        if c in ['GR', 'GB']:   # Is this a joker card?
            rank = c
            suite = ''
        else:
            suite = c[-1]
            if suite not in ['S', 'H', 'C', 'D']:
                raise ValueError("Suite must be one of [S, H, D, C]")

            rank = c[:-1]
            if rank not in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                raise ValueError("Rank must be one of [A, 2-10, J, Q, K]")

        self.__rank = rank
        self.__suite = suite

    def __repr__(self):
        return self.__rank + self.__suite

    @property
    def rank(self):
        return self.__rank

    @property
    def suite(self):
        return self.__suite


def main():
    c = Card("9")
    print c.rank


if __name__ == "__main__":
    main()
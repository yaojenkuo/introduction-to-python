from random import choice

class Casino:
    def toss_a_coin(self):
        coin = ['Head', 'Tail']
        return choice(coin)
    def roll_a_dice(self):
        dice = range(1, 7)
        return choice(dice)
    def deal_a_card(self):
        suits = ['spades', 'hearts', 'diamonds', 'clubs']
        ranks = ['ace', 'jack', 'queen', 'king'] + list(range(2, 11))
        card_deck = []
        for s in suits:
            for r in ranks:
                card = '{} of {}'.format(r, s)
                card_deck.append(card)
        return choice(card_deck)
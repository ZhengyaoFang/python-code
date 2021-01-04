import random


class Card(object):
    """一张牌"""

    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def face(self):
        return self._face

    @property
    def suite(self):
        return self._suite

    def __str__(self):
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return self.__str__()


class Poker(object):
    """一副牌"""

    def __init__(self):
        self._cards = [Card(suite, face)
                       for suite in '♠♥♣♦'
                       for face in range(1, 14)]
        self._current = 0

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        """洗牌（随即乱序）"""
        self._current = 0
        random.shuffle(self._cards)

    @property
    def next(self):
        """发牌"""
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌"""
        return self._current < len(self._cards)


class Player(object):
    """玩家"""

    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []
        self._cards_gained = []
        self._is_dead = False

    @property
    def name(self):
        return self._name

    @property
    def is_dead(self):
        return self._is_dead

    def get(self):
        """拿牌"""
        self._cards_on_hand = list(map(int, input('请按顺序输入手牌，中间以空格分开，回车结束:').split()))
        print('%s的手牌为：' % self.name, self._cards_on_hand)

    def put_card(self, table_card):
        if len(self._cards_on_hand) != 0:
            table_card.append(self._cards_on_hand[0])
            print(self.name, 'put the card', self._cards_on_hand[0])
            self._cards_on_hand.pop(0)
            print('And now the table cards are:', table_card)

        elif len(self._cards_gained) != 0:
            self._cards_on_hand.extend(self._cards_gained)
            self._cards_gained.clear()
            table_card.append(self._cards_on_hand[0])
            print(self.name, 'put the card', self._cards_on_hand[0])
            self._cards_on_hand.pop(0)
            print('And now the table cards are:', table_card)

        else:
            print(self._name, ':You lost!')
            self._is_dead = True

    def inspect(self, table_card):
        if len(table_card) != 1:
            for index in range(len(table_card)-1):
                if table_card[-1] == table_card[index]:
                    gain = table_card[index: len(table_card)]
                    print(self._name, ':Here is also a %d,and' % table_card[-1], gain, 'is mine!')
                    gain.extend(self._cards_gained)
                    self._cards_gained.extend(gain)
                    del table_card[index:]
                    print('Then here are', table_card, 'on the table')
                    return True
        return False











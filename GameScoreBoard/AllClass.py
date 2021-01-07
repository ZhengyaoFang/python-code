"""
名称：为游戏储存高分（高分条目）
Eve
"""


class GameEntry(object):
    """高分榜的一个游戏条目"""
    def __init__(self, name, score):
        self._name = name
        self._score = score

    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._score

    def __str__(self):
        return '({0},{1})'.format(self._name, self._score)


class ScoreBoard(object):
    """高分榜"""

    def __init__(self, capacity=10):
        self._board = [None]*capacity       # 容量
        self._len = 0                       # 实际个数

    @property
    def len(self):
        return self._len

    def __getitem__(self, k):
        return self._board[k]

    def __str__(self):
        return '\n'.join(str(self._board[j]) for j in range(self._len))

    def add(self, entry):
        score = entry.score
        good = self._len < len(self._board) or score > self._board[-1].score
        if good:
            if self._len < len(self._board):
                self._len += 1

            j = self._len - 1
            while j > 0 and self._board[j-1].score < score:
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry






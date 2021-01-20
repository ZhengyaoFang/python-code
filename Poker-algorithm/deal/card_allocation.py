"""
牌模型：
    ->由 card[i]:(0<=i<=51) 代表五十二张牌,card为整数数列。
    ->card[i]//4+1 代表牌值不分花色的，即 1-A，2-2,3-3,...,10-10,11-J,12-Q,13-K
    ->card[i] % 4 代表该牌的花色：0-红心，1-黑桃，2-方片，3-梅花
"""
from random import shuffle
import time


"""顺序创建一整副牌"""
card = [x for x in range(52)]

# print(card)
# 检查正确

"""洗牌"""
shuffle(card)
# print(card)     # 每次跑完结果都不一样

"""
三种功能牌：
    ->底牌：两张*n
    ->公共牌1：三张（翻）
    ->公共牌2：两张（不翻）
"""

"""发牌"""
player1_card = []
player2_card = []       # 暂定双人对战，1代表自己
public_card = []        # 公共牌

"""发牌"""
for i in range(2):
    player1_card.append(card.pop(-1))
for i in range(2):
    player2_card.append(card.pop(-1))
# print(player1_card, player2_card)     # 测试

for i in range(5):                      # 公共牌
    public_card.append(card.pop(-1))


def display(cards):
    """传入原始牌值序列，显示字符型牌面"""

    # 字典对应字符型牌面花色
    face_str = dict([(1, "A"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"), (7, "7"), (8, "8"), (9, "9"), (10, "10"), (11, "J"), (12, "Q"), (13, "K")])
    suite = dict([(0, "♠"), (1, "♥"), (2, "♣"), (3, "♦")])

    for x in cards:
        print(face_str[x // 4 + 1], suite[x % 4])


# display(player1_card)     #Test











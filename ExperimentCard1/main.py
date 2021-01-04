from Class import Player
import random


def main():
    print('Game Start!')
    table_card = []
    """
    自动洗牌
    poker = []
    for i in range(13):
        for j in range(4):
            poker.append(i+1)

    poker.extend([14, 14])
    random.shuffle(poker)
    """
    number = int(input('请输入玩家人数：'))
    player = []
    for i in range(number):
        name = input('请输入玩家%d姓名：' % (i+1))
        player.append(Player(name))

    for i in range(number):
        player[i].get()

    while True:
        # 判断是否有胜利者出现
        if len(player) == 1:
            print('Game Over!The victory is %s!' % player[0].name)
            break
        input('Print any key to continue……')
        # 轮流行动：
        for num in player:
            num.put_card(table_card)
            while num.inspect(table_card):
                num.put_card(table_card)

            if num.is_dead:
                player.remove(num)


if __name__ == '__main__':
    main()






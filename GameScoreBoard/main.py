from AllClass import *


def menu():
    print('     Menu        \n'
          '1.查看榜单\n'
          '2.录入数据\n'
          '3.查询名次信息\n'
          '0.退出系统\n')


def main():
    print('高分榜')
    capacity = int(input('请输入榜容量大小：'))
    board = ScoreBoard(capacity)
    while True:
        try:
            menu()
            direction = int(input())
            if direction == 1:
                print(board)
            elif direction == 2:
                name = input('name:')
                score = input('score:')
                new_entry = GameEntry(name, score)
                board.add(new_entry)
                print('done well!')
            elif direction == 3:
                index = int(input('查询的名次：'))-1
                if index <= board.len:
                    print(board[index])
                else:
                    print('Waiting for u!')
            elif direction == 0:
                break
            else:
                print('illegal value!')
        finally:
            pass

if __name__ == '__main__':
    main()





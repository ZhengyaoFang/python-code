import BankClass
import copy
"""面向对象编程实践之银行管理系统"""
cards_in_bank = []


def menu():
    print('欢迎使用银行系统一代目！')
    print('功能目录如下：'
          '1.开户'
          '2.查询'
          '3.取款'
          '4.存款'
          '5.转账'
          '6.锁定'
          '7.解锁'
          '0.退出')
    choice = int(input('请输入指令：'))
    if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
        return choice
    else:
        print('请输入正确指令！')
        return None


def main():
    global cards_in_bank
    while True:
        working_bank = BankClass.Bank(cards_in_bank)
        choice = None
        choice = menu()
        if choice == 1:
            working_bank.create_a_card()
        elif choice == 2:
            working_bank.check_for_balance()
        elif choice == 3:
            working_bank.get_money()
        elif choice == 4:
            working_bank.deposit()
        elif choice == 5:
            working_bank.transfer()
        elif choice == 6:
            working_bank.lock()
        elif choice == 7:
            working_bank.unlock()
        elif choice == 0:
            cards_in_bank = copy.deepcopy(working_bank.exit())
            working_bank = None
            break
        working_bank = None




if __name__ == '__main__':
    main()

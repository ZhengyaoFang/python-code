import random as r


class Bank(object):
    """银行管理系统"""

    def __init__(self, cards_in_bank):
        # self._users = []
        self._account_numbers = [x._account for x in cards_in_bank]
        self._cards = cards_in_bank
        self._the_using_card = None

    def create_a_card(self):
        name = input('请输入姓名：')
        id_card = input('请输入身份证号：')
        phone_number = input('请输入手机号：')
        pre_store = int(input('预存金额：'))
        password = input('请输入初始密码：')
        account_number = r.randint(100000, 1000000)
        self._account_numbers.append(account_number)
        print('该卡卡号为：', account_number)
        self._cards.append(Card(account_number, password, pre_store, name, id_card, phone_number))

    def can_sign_in(self):
        is_there_account = False
        the_card = None
        the_input_account = ''
        for i in range(3):
            input_account = int(input('请输入卡号：'))
            if input_account in self._account_numbers:
                the_input_account = input_account
                is_there_account = True
                break
            print('输入错误！')

        if is_there_account:
            for card in self._cards:
                if card._account == the_input_account:
                    self._the_using_card = card
                    break
            if self._the_using_card._is_locked:
                print('此卡已被锁定，请返回主页面进行解锁！')
                return False
            else:
                for j in range(3):
                    input_password = input('请输入密码：')
                    if input_password == self._the_using_card._password:
                        return True
                    print('错误！')
                self._the_using_card._is_locked = True
                print('输入密码错误次数过多！此卡已被锁定。若要解锁请返回主页进行解锁！')
                return False
        else:
            print('错误！即将返回主页面！')

    def check_for_balance(self):
        if self.can_sign_in():
            print('您的余额为：', self._the_using_card.balance)
            return True
        return False

    def get_money(self):
        if self.check_for_balance():
            money_wanted = int(input('请输入取款金额：'))
            if 0 <= money_wanted < self._the_using_card.balance:
                self._the_using_card._balance -= money_wanted
                print('成功取款', money_wanted)
                print('卡内余额为：', self._the_using_card.balance)
            else:
                print('卡内余额不足！即将返回主页面！')

    def deposit(self):
        if self.check_for_balance():
            amount = int(input('请输入存款金额：'))
            if amount > 0:
                self._the_using_card._balance += amount
                print('卡内余额为：', self._the_using_card.balance)
            else:
                print('不合法！')

    def transfer(self):
        if self.check_for_balance():
            to_card_account = int(input('请输入入账账户：'))
            to_card = None
            find = False
            for card in self._cards:
                if card._account == to_card_account:
                    to_card = card
                    find = True
                    break
            if find:
                amount = int(input('请输入转账金额：'))
                if 0 <= amount < self._the_using_card.balance:
                    self._the_using_card._balance -= amount
                    to_card._balance += amount
                    print('成功转账：', amount)
                    print('卡内余额为：', self._the_using_card.balance)
                else:
                    print('卡内余额不足！')
            else:
                print('该账户不存在！')

    def lock(self):
        if self.can_sign_in():
            self._the_using_card._is_locked = True
            print('成功锁定！')

    def unlock(self):
        for i in range(3):
            input_account = int(input('请输入卡号：'))
            if input_account in self._account_numbers:
                the_input_account = input_account
                is_there_account = True
                break
            print('输入错误！')

        if is_there_account:
            for card in self._cards:
                if card._account == the_input_account:
                    self._the_using_card = card
                    break
            password = input('请输入密码以解锁！')
            if password == self._the_using_card._password:
                self._the_using_card._is_locked = False
                print('解锁成功！')
            else:
                print('解锁失败！')

    def exit(self):
        return self._cards


"""
class User(object):
    ""用户类型""
    def __init__(self, name, id_card, phone_number):
        self._name = name
        self._id_card = id_card
        self._phone_number = phone_number
        self._package = []

    def get_a_card(self, account_numbers):
        pre_store = int(input('预存金额：'))
        password = input('请输入初始密码：')
        account_number = r.randint(100000, 1000000)
        print('该卡卡号为：', account_number)
        self._package.append(Card(account_number, password, pre_store, self._name, self._id_card, self._phone_number))
        return account_number
"""


class Card(object):
    """银行卡类型"""

    def __init__(self, account_number, password, pre_store, user_name, user_id, user_phone):
        self._user_name = user_name
        self._user_id = user_id
        self._user_phone = user_phone
        self._account = account_number
        self._password = password
        self._balance = pre_store
        self._is_locked = False

    @property
    def balance(self):
        return self._balance

#계좌 클래스
class Account:
    # __ => private, _ => proctatid
    def __init__(self, bank, id, name, balance):
        # 속성
        self._bank = bank
        self._id = id
        self._name = name
        self._balance = balance

    # 기능
    def deposit(self, balance):
        self._balance += balance

    def withdraw(self, balance):
        self._balance -= balance

    def show(self):
        print('--------------------')
        print('은행명 :', self.__bank)
        print('계좌번호 :', self.__id)
        print('입금주 :', self.__name)
        print('현재잔액 :', self.__balance)


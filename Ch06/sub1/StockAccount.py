from Ch06.sub1.Account import Account

class StockAccount (Account):
    def __init__(self, bank, id, name, balance, stock, amount, price):
        super().__init__(bank, id, name, balance)

        self.stock = stock
        self.amount = amount
        self.price = price


    #주식 팔기
    def sell(self, amount, price):
        #self.__balance += self.amount * self.price  # error : 부모 클래스가 private로 선언되어 있기 때문에
        self._balance += self.amount * self.price #error


    def buy(self, amount, price):
        self._balance -= self.amount * self.price #error

    #잔액조회
    def show(self):
        print('--------------------')
        print('은행명 :', self._bank)
        print('계좌번호 :', self._id)
        print('입금주 :', self._name)
        print('현재잔액 :', self._balance)
        print('주식종목 :', self.stock)
        print('주식수량 :', self.amount)
        print('주식가격 :', self.price)
        print('--------------------')





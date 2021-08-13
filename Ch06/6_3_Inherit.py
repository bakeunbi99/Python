"""
날짜 : 2021/08/12 14:56
이름 : 박은비
내용 : 파이썬 상속 실습하기 교재 p163
"""

from Ch06.sub1.StockAccount import StockAccount

kb = StockAccount('KB증권', '101-121-100', '김유신', 30000, '삼성전자', 1, 80000)
kb.deposit(70000)
kb.withdraw(5000)
kb.show()
kb.sell(1, 80000)
kb.show()






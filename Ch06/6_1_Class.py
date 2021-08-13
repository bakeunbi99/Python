"""
날짜 : 2021/08/11 16:42
이름 : 박은비
내용 : 파이썬 객체 지향 프로글밍 실습하기 교재 p148
"""
from Ch06.sub1.Car import Car
from Ch06.sub1.Account import Account

# 객체 생성
bmw = Car('525d', '흰색', 5000) #Python에서는 new() 키워드가 없음.
bmw.speedDown()
bmw.speedUp()
bmw.show()

benz = Car('벤츠', '검정색', 5000)
benz.speedUp()
benz.show()

kb = Account('국민은행', '101-12-1111', '김유신', 10000)
kb.deposit(40000)
kb.withdraw(5000)
kb.show()

wr = Account('우리은행', '105-11-7878', '김춘추', 30000)
wr.deposit(10000)
wr.withdraw(20000)
wr.show()





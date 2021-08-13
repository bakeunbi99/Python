"""
날짜 : 2021/08/12
이름 : 박은비
내용 : 실습예제 2
"""

sum = 0
for k in range(1, 11):
    if k%2 ==0 or k%3==0:
        sum += k

print('2와 3 배수의 정수의 합 : ', sum)

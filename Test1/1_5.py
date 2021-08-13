"""
날짜 : 2021/08/12
이름 : 박은비
내용 : 실습예제 4
"""

str = '12345'
sum = 0

for i in range(len(str)):
    num = int(str[i])
    sum += num

print('합 : ', sum)
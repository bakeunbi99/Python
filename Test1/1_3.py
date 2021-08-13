"""
날짜 : 2021/08/12
이름 : 박은비
내용 : 실습예제 3
"""

sum = 0

for i in range(1, 11):
    for j in range(1, i+1):
        sum += j
        print('%d' % j, end='+')
    print()

print('총합 : ', sum)
"""
날짜 : 2021/08/12
이름 : 박은비
내용 : 실습예제 4
"""

for i in range(1, 7):
    for j in range(1, 7):

        tot = i + j

        if tot == 6:
            print('첫번째 주사위 : %d, 두 번째 주사위 : %d' %(i, j))


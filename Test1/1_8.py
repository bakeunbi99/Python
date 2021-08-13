"""
날짜 : 2021/08/12
이름 : 박은비
내용 : 실습예제
"""

scores = [62, 82, 76, 88, 54, 92]

max = scores[0]
min = scores[0]

for socre in scores:

    if max < socre:
        max = socre

    if min > socre:
        min = socre

print('최대값 : ', max)
print('최소값 : ', min)

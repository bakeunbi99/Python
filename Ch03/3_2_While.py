"""
날짜 : 2021 /08/10 14:53
이름 : 박은비
내용 : 파이썬 if문 실습하기 교재 p64
"""

# while
num = 1
while num < 5:
    print('%d회', num)
    num += 1
print('합은', num)

# 1부터 10까지 합
tot, k = 0, 1

while k <= 10:
    tot += k
    k+=1
print('1부터 10까지의 합:', tot)

# 1부터 10까지 짝수합
total, j = 0, 1
while j <= 10:
    # j가 짝수이면
    if j % 2 == 0:
        total += j
    j += 1

print('1부터 10까지의 짝수합 :', total)

# 1부터 10까지 홀수합
total, j = 0, 1
while j <= 10:
    # j가 홀수 이면
    if j % 2 != 0:
        total += j
    j += 1

print('1부터 10까지의 짝수합 :', total)

# break
i = 1

while True:

    if i % 5 == 0 and i % 7 ==0:
        break
    i += 1

print('5와 7의 최소공배수 : ', i)

# continue
sum, n = 0, 1

while n <= 10:
    n += 1
    #n이 홀수일 경우
    if n % 2 == 1:
        continue

    sum += n

print('1부터 10까지 짝수 합 : ', sum)



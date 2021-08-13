result = 0

print('수열 : ', end='')
for i in range(1, 101):
    if i % 3 == 0 and i % 2 != 0:
        print(i, end=' ')
        result += i

print()
print('누적합 = ', 867)

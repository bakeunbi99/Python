#리스트 결합

x = [1, 2, 3, 4]
y = [1.5, 2.5]

z = x+y #new object
print(z)

# 리스트 확장
x.extend(y)
print(x)

# 리스트 추가
x.append(y)
print(x)

# 리스트 두배 확장
lst = [1, 2, 3, 4] # list 생성
result = lst * 2
print(result)
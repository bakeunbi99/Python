# 리스트 두배 확장
lst = [1, 2, 3, 4] # list 생성
result = lst * 2

# 리스트 정렬
print(result)
result.sort() # 오름차순
print(result)
result.sort(reverse=True) #내림차순
print(result)

#리스트 요소 검사
import random
r = [] #빈 리스트
for i in range(5) :
    r.append(random.randint(1, 5))

print(r)
if 4 in r : 
    print('있음')
else:
    print('없음')
# SET
# 중복을 허용하지 않는다
# 순서가 없기 때문에 색인(index)를 사용할 수 없다.
# 객체에서 제공하는 함수를 이용하여 추가, 삭제 및 집합 연산등이 가능하다.


#중복 불가
s = { 1, 2, 5, 3, 1 }
print(len(s))
print(s)

for d in s:
    print(d, end=' ')
print()

# 집합 관련 함수
s2 = {3, 6}
print(s.union(s2)) # 합집합
print(s.difference(s2)) # 차집합
print(s.intersection(s2)) # 교집합

# 추가, 삭제 함수
s3 = {1, 3, 5}
print(s3)

s3.add(7)
print(s3)

s3.discard(3)
print(s3)



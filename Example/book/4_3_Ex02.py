# 튜플 자료형 변환
lst = list(range(1, 6))
t3 = tuple(lst)
print(t3)

#튜플 관련 함수
print(len(t3), type(t3))
print(t3.count(3)) # 원소 3의 개수를 반환받아서 출력
print(t3.index(4)) # index() 함수에 의해서 원소 4의 색인(위치)를 반환받아서 출력


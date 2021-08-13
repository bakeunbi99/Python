"""
일자 : 2021/08/10 16:53
이름 :
내용 : 파이썬 자료구조 Tuple 실습하기 교재 p92
"""

#Tuple(고정 리스트)
tuple1 = (1, 2, 3, 4, 5)
print('tuple1 type : ', type(tuple1))
print('tuple1[0] : ', tuple1[0])
print('tuple1[2] : ', tuple1[2])
print('tuple1[3] : ', tuple1[3])


tuple2 = ('서울', '대전', '대구', '부산', '광주')
print('tuple1 type : ', type(tuple2))
print('tuple2[0] : ', tuple2[0])
print('tuple2[2] : ', tuple2[2])
print('tuple2[3] : ', tuple2[3])

#튜플 수정, 삭제
# 괄호 생략 가능
tuple3 = 1, 2, 3, 4, 5

#error -> 고정 리스트 이기 때문에 수정 X
# tuple3[0] = 7
# print('tuple3 : ', tuple3)


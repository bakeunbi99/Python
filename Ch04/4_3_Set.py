"""
일자 : 2021/08/10 16:59
이름 : 박은비
내용 : 파이썬 자료구조 set 실습하기 교재 p96
"""
#SET 중복허용x, 순서 상관 x

# Set
set1 = { 1, 2, 3, 4, 5, 3, 2 }
print('set1 type : ', type(set1))
print('set1  : ', set1)

set2 = set('Hello World')
print('set2 type : ', type(set2))
print('set2  : ', set2)


# 리스트 변환 후 출력
list1 = list(set1)
print('list1 type : ', type(list1))
print('list1  : ', list1)
print('list1[0]  : ', list1[0])
print('list1[3]  : ', list1[3])

list2 = list(set2)
print('list2 type : ', type(list2))
print('list2  : ', list2)
print('list2[0]  : ', list2[0])
print('list2[3]  : ', list2[3])

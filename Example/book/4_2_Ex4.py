# 단일 리스트 객체 생성
num = ['one', 'two', 'three', 'four']
print(num) #['one', 'two', 'three', 'four']

# 리스트에 원소 추가
num.append('five') #추가
print(num) #['one', 'two', 'three', 'four', 'five']

# 원소 리스트 삭제
num.remove('five')
print(num)

# 리스트 원소 수정
num[3] = '4' #수정
print(num)

# 리스트 원소 삽입
num.insert(0, 'zero') #삽입
print(num)
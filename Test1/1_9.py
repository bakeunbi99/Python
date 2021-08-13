"""
날짜 : 2021/08/12
이름 : 박은비
내용 : 실습예제
"""

dataset = [3, 5, 1, 2, 4] # type list
size = len(dataset) # type int


for i in range(size-1): #5-1
    for j in range(i+1, size):

        if dataset[i] > dataset[j]:
            tmp = dataset[i]
            dataset[i] = dataset[j]
            dataset[j] = tmp

    print('%d Round : %s' % (i, dataset))

print('Result : ', dataset)
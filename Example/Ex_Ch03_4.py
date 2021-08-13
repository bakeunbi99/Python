multiline = "안녕하세요. 파이썬 세계로 오신걸 환영합니다. 파이썬은 비단뱀 처럼 매력적인 언어입니다."
str = multiline.split(' ')

print('글자수 ', len(multiline))
print('단어 개수 ', len(str))
print(str)

count = 0
for i in range(len(str)):
    print(str[i])
    count += 1

print('단어 개수', count, '개')

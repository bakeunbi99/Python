"""
날짜 :  2021/08/21 16:10
이름 : 박은비
내용 : 파이썬 파일 입출력 실습 교재 p217
"""

# 파일 읽기 'r'
file1 = open('./Text1.txt', 'r')
line = file1.readline()

print(line)
file1.close()


file2 = open('./Text1.txt', 'r')

while True:
    line = file2.read()

    if not line:
        # 파일의 내용이 없으면
        break

    print(line)

file2.close()


# 파일쓰기 'w'
file3 = open('./Text2.txt', 'w', encoding='UTF-8')
file3.write('안녕하세요. \n')
file3.write('반갑습니다. \n')
file3.write('감사합니다.. \n')
file3.close()








fat = input('지방의 그램을 입력하세요 : ')
carbohydrate = input('탄수화물의 그램을 입력하세요 : ')
protein = input('단백질의 그램을 입력하세요 : ')

fat = int(fat)
carbohydrate = int(carbohydrate)
protein = int(protein)

kcal = (fat * 9) + (protein * 4) + (carbohydrate * 4)
print('총 칼로리 : ', kcal, 'cal')

test = input('test 그램을 입력하세요 : ')
result = (test) * 9
print('result : ', result)



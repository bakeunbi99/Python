gimKg = int(input('짐의 무게는 얼마입니까?'))

su = 10000
gim = gimKg / 10
suGim = su * int(gim)


if gimKg >= 10:
    print('수수료는 %d원 입니다' % suGim)
else:
    print('수수료는 없습니다.')

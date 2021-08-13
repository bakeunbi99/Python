#sub1(패키지)의 모듈 파일.
#자동차 클래스(모듈) 정의
class Car:

    #init : 생성자.
    def __init__(self, model, color, price): #init함수에 속성을 정의한다.
        # 속성
        self.model = model
        self.color = color
        self.price = price


    # 기능
    # 속도 올리기
    def speedUp(self):
        print('%s speed Up... ' % self.model)
    # 속도 내리기
    def speedDown(self):
        print('%s speed Down... ' % self.model)
    # 보여주기
    def show(self):
        print('차량 명 : ', self.model)
        print('차량 색 : ', self.color)
        print('차량 가격 : ', self.price)
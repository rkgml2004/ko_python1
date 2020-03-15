
# 작업 순서 
# 1. 모듈 또는 클래스 import
# 2. main() 메서드 만들기 
#     인스턴스 생성
# 3. 이 모듈이 단독으로 사용되면 main()를 호출하라.
#    if __name__ == "__main__":
#    main()

# 코딩 하기 

# calss 선언하는 부분 시작
# .first = 공개, .__first = 비공개
class FourCal:
    def setdata(self, first, second):
        self.__first = first
        self.second = second

    def add(self):
        result = self.__first + self.second
        return result

    def mul(self):
        result = self.__first * self.second
        return result

    def minus(self):
        result = self.__first - self.second
        return result

    def div(self):
        result = self.__first / self.second
        return result
# class 선언 종료


# 인스턴스 만들기
# fourcal 이라는 인스턴스를 만든다.

fourcal = FourCal()
fourcal.setdata(2, 4)

cal1 = fourcal.add()
print("add : ", cal1)  # add : 3

cal2 = fourcal.mul()
print("mul : ", cal2)

cal3 = fourcal.minus()
print("minus : ", cal3)

cal4 = fourcal.div()
print("div : ", cal4)

import math  # P1 = 3.14159 변수를 사용하기 위해서 import


def circle(radius):
    area = math.pi * radius * radius
    circum = 2 * math.pi * radius
    return(area, circum)  # 튜플 자료구조 1개를 리턴하는 것

def main():
    radius = float(input("원의 반지름을 입력하시오."))  # 문자열을 실수로 변환


    # 원의 넓이와 둘레를 계산
    (x, y) = circle(radius)  # x : 면적, y: 둘레


    tmp = ("원의 넓이는 %10.4f , 둘레는 %10.4f 이다.") % (x, y)
    print(tmp)

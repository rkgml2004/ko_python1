# 사용자 함수 만들기
# 정수를 입력받아서 제곱한 값을 반환하는 square() 함수를 만들어 보기

# 함수정의
# n : 매개변수


def square(n):

    return n**2  # 결과 변환


# 함수 호출
val = square(10)  # 100
print("10의 제곱")


# 함수 정의
# x : 매개변수
# y : 매개변수

def getmax(x, y):  # getmax : 최대함수
    result = None  # None : 값이 없다.

    if x > y:
        return x  # x 반환
        result = x
    else:
        return y  # y 반환
        result = y

    return result


n1 = input("첫번째 정수 입력:")
n1 = int(n1)


def myinput(mesg):
    try:
        n1 = input(mesg)
        n1 = int(n1)

    except ValueError as ex:
        print(ex)

    return n1


# 입력처리
n1 = myinput("첫번째 정수 입력: ")

n2 = input("두번째 정수 입력:")
n2 = int(n2)


# 최대값 출력
val1 = getmax(n1, n2)
print(val)

#main() 함수 사용 
def main() : 
    
    main()

# x = input("시작값 입력>>>")  # 문자열   15
# x = int(x)  # 문자열을 정수로 바꾼다.

# y = input("종료값 입력>>>")  # 문자열   11
# y = int(y)  # 문자열을 정수로 바꾼다.

# 시작값이 종료값보다 크다면 값을 바꾸고
# 아니면 pass

# if x > y:
# 값을 바꾸고
# temp = x
# x = y
# y = temp
# else:
# pass

# sum = 0
# for z in range(x, y+1, 1):
# sum = sum + z   # x부터 y까지 1씩 증가하면서 합계를 구한다.

# 1부터 4까지의 합계는 10 입니다 <--- 문자열 포맷팅 연산자 사용.
# str = "%s 부터 %s까지의 합계는 %s입니다." % (x, y, sum)  # 1부터 4까지의 합계

# 출력
# print(str)

x = input("시작단수")
x = int(x)

y = input("종료단수")
y = int(y)

if x < y:
    temp = x
    x = y
    y = temp

for i in range(11, 16, 1):
    for j in range(1, 10, 1):
        str = "%2s*%s=%3s" % (i, j, i*j)  # %2s, %3s 는 자리수 맞취기 위해서
        print(str, end=" ")

        # j 가 9이면 마침표를 찍고, 아니면 콤마를 출력하시오.
        if j == 9:
            print(str, end=".")
        else:
            print(str, end=",")

        # 줄바꿈 필요
    print()

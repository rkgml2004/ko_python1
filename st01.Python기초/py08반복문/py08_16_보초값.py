# 교재 72, 78, 80, 134p 참조

# while 문을 사용하여 합계를 구하시오.
# 무한 반복과 반복문(루프) 탈출을 결합한 예제
# 교재 134p


# 무한 반복문은 조건식을 True 로 하면 된다.
# 루프 탈출은 break 를 사용하면 된다.


sum = 0
count = 0
print("종료하려면 음수를 입력하시오.")
while True:  # 무한 루프
    입력 = input("성적을 입력하시오,")
    # 정수로 변환
    입력 = int(입력값)
    # 입력값이 음수이면 반복물을 종료하시오.  break
    if 입력 < 0:
        break
    else:
        count = count + 1  # 입력 횟수

    # 합계를 구한다.
    sum = sum + 입력값

# 평균를 계산한다.
평균값 = sum / count

# 평균를 출력한다.
str = "성적의 평균은 %s 입니다." % 평균값
print(str)

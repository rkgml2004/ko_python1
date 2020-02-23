
while True:
    x = input("시작단수")
    x = int(x)

    y = input("종료단수")
    y = int(y)
    
    if x > y:
          temp = x
          x = y
          y = temp
          
    for i in range(1, 10, 1):
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


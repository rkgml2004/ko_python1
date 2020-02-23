def get_sum(x, y):
    sum3 = 0
    for i in range(x, y + 1, 1):
        sum3 = sum3 + i
    str = "%s부터 %s까지의 합계 :  " % (x, y)
    print(str, sum3)

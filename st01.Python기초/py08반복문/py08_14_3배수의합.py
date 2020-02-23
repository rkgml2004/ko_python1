# 1부터 100 사이의 모든 3의 배수의 합은 1683입니다.
# 3의 배수는 나머지 연산자를 이용하여 구한다.
# 3의 배수이면 sum 하고 아니면 pass 한다.


sum = 0
for i in range(1, 101, 1):
    if i % 3 == 0:
        sum = sum + i
    else:
        pass
print(sum)


# 나머지 연산자 %


i = 1
sum = 0
while i <= 100:
    if i % 3 == 0:
        sum = sum + i
    else:
        pass
    i = i + 1
str = "%s 부터 %s 사이의 3의 배수의 합은 %s 입니다." % (1, 100, sum)
print(str)

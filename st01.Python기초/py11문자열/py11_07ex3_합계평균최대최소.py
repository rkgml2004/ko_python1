temp3 = "74 874 9883 73 9 73646 774"

lst = temp3.split(" ")
print(type(lst), lst)


for i in range(0, len(lst), 1):
    lst[i] = int(lst[i])
print(type(lst), lst)

# 합계
print("합계", sum(lst))


# 평균
print("평균", sum(lst) / len(lst))


# 최대값
print("max", max(lst))  # 20


# 최소값
print("min", min(lst))  # 10

x = input("첫번째수를 입력하세요")
x = int(x)

y = input("두번째수를 입력하세요")
y = int(y)

z = input("세번째수를 입력하세요")
z = input(z)
#중립적 if 방식
if x > y  : 
    print(x)
    # x와 z 비교 
    if x < z : 
        print(z)
    else :
        print (x)
else : 
    # y와 z 비교
    if  y < z :
        print(z)
    else : 
        print(y)

#연속적 if 방식

if x > y and z > x : 
    print(x)
elif y < z : 
    print(z)
else : 
    print(y)
    
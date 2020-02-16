#불린 타입
print(not True)
print(not False)

x = 3
y = 4

r = ((x==3) and (y == 3))
print("(x==3) and (y==3) : " , r)

r = ((x==3) and (y!=3))
print("(x==3) and (y!=3) : " , r)

r = ((x==3) or (y==3))
print("(x==3) or (y==3) : " , r)

r = ((x==3) or (y==4))
print("(x==3) or (y==4) : ", r)

r = ((x!=3) or (y==4))
print("(x!=3) or (y==4) : " , r)

r = ((x!=3) or (y!=4))
print("(x!=3) or (y!=4) : " , r)

 # 변수 선언과 초기화
 
 
a = 3
b = 4
print((a==y) and (a!=b))
print((x>y) or (x<y))
print((x >= y) or (x <=y))
print((x==y) and (x!=y) or (x<y))
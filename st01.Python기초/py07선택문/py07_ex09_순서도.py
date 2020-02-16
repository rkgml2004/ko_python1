A = input("정수입력")
B = input("정수입력")

#문자열에는 *, + 연산자만 있고, / 연산자는 없다. 
try:
 A = int(A)
 B = int(B)
 avg = (A+B) / 2

except ValueError



if avg >= 160 :
    print("합격")
else : 
    print("불합격")
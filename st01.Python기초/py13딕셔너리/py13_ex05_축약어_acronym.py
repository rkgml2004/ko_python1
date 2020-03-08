# 작업순서
# 1. 문자열을 split( ) 해서 리스트로 만든다.
# 2. 반복문을 사용하여 array 리스트를 루프를 돌면서 딕셔너리 table에서 찾는다.
# 3. 찾았다면 바꾼다. = replace( )
# 4. 출력

# 0. 문자열을 입력하시오.
str = input("문자열을 입력하세요.")

# 1. 2. 문자열 나눠서 리스트로 만들기.  / 반복한다.
a = "TX Mr. Park! Thanks Mr. Park!"
b = a.split()
# 2가지 방법
# array = str.split("")
# for i in range (0, len(array), 1):
#print (array[i])

# for i in array :
#print (i)

print(b)

result = "" #출력할 문자열 

# 3. 바꾼다.
# array[0] = table에서 찾기 = .get( ) , in
value = array.get(i)  # value 값이 none 이면 키가 없다는 의미
if value == None:
    print("")
else:
    print(".")
    print(value)




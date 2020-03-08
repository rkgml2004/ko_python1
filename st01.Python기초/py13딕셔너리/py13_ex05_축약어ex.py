table = {"B4": "Before",
         "TX": "Thanks",
         "BBL": "Be Back Later",
         "BCNU": "Be Seeing You",
         "HAND": "Have A Nice Day"}

str = input("문자열을 입력하세요.")

array = str.split(" ")
for i in array : 
    print(i)


value = table .get(i)  # value 값이 none 이면 키가 없다는 의미
if value == None:
    result = result + i + " "       # " " 공백 
else:
    result = result + value +  " "
    
print (result)
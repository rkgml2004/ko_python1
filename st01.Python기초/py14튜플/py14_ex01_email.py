adress = input("이메일 주소를 입력하시오. ")

(id, domain) = adress.split("@")

print(adress)
print(" " + id)
print(" " + domain)


arr = adress.split("@")
(id, domain) = arr  # id  = arr[0] , domain  = arr[1]
print(adress)
print(" " + id)



#readline() 파일에서 한 줄씩 읽기
#########################
print("readline() 파일에서 한 줄씩 읽기")
pfr = open("./file/phones/txt", "r")

s = pfr.readline()
print(s)
s = pfr.readline()
print(s)
s = pfr.readline()
print(s)


pfr.close()

#반복문으로 파일에서 읽어서 모니터에 출력하기
print("반복문으로 파일에서 읽어서 모니터에 출력하기")
pfr = open("./file/phone.txt", "r") 

line = pfr.readline()
while line != "":
    print(s)
    line = pfr.readline
#########################
##

#########################
##

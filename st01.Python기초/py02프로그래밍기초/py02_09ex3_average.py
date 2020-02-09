value1 = input("첫번째 과목 점수를 입력하세요")
value1 = int(value1)

value2 = input("두번째 과목 점수를 입력하세요")
value2 = int(value2)

sum = value1 + value2
average = sum / 2 

print('------------------')

if average >= 95:
    print("very Good")
else :
    print("just Good")
    
print("------------------")
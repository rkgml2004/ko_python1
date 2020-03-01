
# 1. List 만들기.
# 2. 학생수 입력 받기. 최소 3명이상
# 3. 학생 성적 입력 받기. 몇번 입력받아야 하는가?
# 4. list에 입력 받은 학생 성적을 추가한다.
# 5. 3번 학생의 성적을 100점으로 바꾸시오.
# 6. list에서 마지막 학생 삭제.
# 7. list에서 0번 값을 출력하시오.
# 8. 평균을 구하고 출력.

for i in range(0, 10, 1):
    print(i)

리스트 = []
count = 0
a = int(input("학생 수를 입력하시오."))

while count < a:
    b = int(input("국어 성적을 입력하시오."))

    리스트.append(b)

    count = count + 1


print(리스트)

#  리스트의 CRUD2S 사용법을 익힌다.
# CRUD2S
# 리스트 추가 (C)==> .append( ), .insert( )
# 리스트 읽기 (R)==> [방번호]
# 리스트 수정 (U) ==> [방번호] = 값
# 리스트 삭제 (D) ==> .pop( )
# 리스트 정렬 (S) ==> sorted( )
# 리스트 정렬 (S)==> .find( ) + 반복문, .rfind( ) + 반복문
pos = 0
value = ""

#  List 선언
리스트 = []


#  C: 추가. 검색: "파이썬 리스트 추가"
#  MILK, BREAD, BUTTER 순으로 추가
리스트.append("MILK")
리스트.append("BREAD")
리스트.append("BUTTER")
print(리스트)


#  APPLE 삽입. 검색: "파이썬 리스트 삽입"
#  특정 위치에 추가하기
#  "BREAD" 앞에 "APPLE" 삽입
#  "BREAD" 가 들어있는 방번호 찾기
pos = 리스트.index("BUTTER")
pos = 리스트.insert(pos, "APPLE")
print(리스트)


#  R: 읽기
#  BUTTER 값을 출력하시오.
#  "BUTTER" 가 들어있는 방번호 찾기
pos = 리스트.index("BUTTER")
print(리스트[pos])

#  U: 수정. 검색: "파이썬 리스트 수정"
#  "BREAD" 를 "GRAPE"로 변경
#  "BREAD" 가 들어있는 방번호 찾기
pos = 리스트.index("BREAD")
리스트[pos] = "GRAPE"
print(리스트)

#  D: 인덱스로 삭제. 검색: "파이썬 리스트 삭제"
#  인덱스를 이용하여 GRAPE 를 삭제
pos = 리스트.index("GRAPE")
리스트.pop(pos)
print(리스트)


#  D: 값으로 찾아서 삭제. 검색: "파이썬 리스트 값으로 삭제"
#  값으로 MILK를 찾아서 삭제하시오
리스트.remove("MILK")
print(리스트)


#  P: 리스트를 for문으로 출력.
#  검색: "파이썬 리스트 for 출력"
#  검색: "파이썬 리스트 크기"
for i in 리스트:
    print(i)

for i in range(0, len(리스트), 1):
    print(i, 리스트[i])

#  P: 리스트를 for-each문으로 출력.
#



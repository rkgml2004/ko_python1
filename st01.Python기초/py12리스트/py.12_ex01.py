#  테스트용 데이터 생성을 위한 코드. 수정하지 마시오.

pos = 0
리스트 = []
리스트.append("APPLE")
리스트.append("BANNA")
print(리스트)

#  S: 검색: "파이썬 리스트 검색

#  첫번째 APPLE을 찾으시오.
pos = 리스트.index("APPLE")
print(리스트[pos])

#  S: 오름차순 정렬. 검색: "파이썬 리스트 오름차순 정렬"
리스트.sort([리스트])
print(리스트[pos])


#  S: 내림차순 정렬. 검색: "파이썬 리스트 내림차순 정렬"
리스트.sort(reverse=True)
print(리스트)

#  검색2. APPLE 이 몇개 있나요?
리스트.count("APPLE")
print(리스트)

#  변환된 배열을 for 문으로 출력.


#  list의 모든 값을 사용하여 삭제하시오
리스트.remove(pos)
print(리스트)

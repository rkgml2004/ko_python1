# 작업순서
# 1. 파일 읽고 문자열에 텍스트 저장
# 줄바꿈을 제거하고 replace 사용
# 2. 문자열을 spli( ) 해서 array 리스트로 만든다.
# 3. 반복문을 사용하여 array 리스트를 루프 돌면서
# 1. 리스트 요소에서 첫글자를 추출한다. 선택연산자 [ ] 사용
# val = array[ i ][ 0 ] 또는 val = i [ 0 ]
# 2. 딕셔너리 table에서 키값중에 val 있는지 찾는다.
# table에서 찾을 때는 get ( ) 매서드나 in 연산자를 사용한다.
# 3. 찾았다면 table[val] = table[val] + "-"
# 아니면 table[val] = "-"
# 4. 찾기가 끝나면 출력한다.

str = """This was a great help.
I applied this method to similiar problem
and rather than concat a SELECT statement
I created an event scheduled every couple
hours to rebuild a view that pivots n amount
of rows from one table into n columns on the other.
It is a big help because before I was rebuilding
the query using PHP on every execution of the SELECT.
Even though views can not leverage Indexes,
I am thinking filtering performance will not
be an issue as the pivoted rows->columns
represent types of training employees at a
franchise have so the view will not ever break
a few thousand rows."""

str = str.replace(" \n", " ").replace(" ", " ")
table = {}
array = str.split(" ")
for i in range(0, len(array), 1):
 # array[0] = This 에서 T만 출력 ==> array[0][0] == T
 # array[1] = was 에서 a만 출력 ==> array[1][1] == a

    key = array[i][0]  # 첫번째 글자 추출
    key = key.upper()  # 대문자로 전환

    tmp = table.get(key)  # table에서 key 값으로 찾기
    if tmp == None:
        # 미존재
        # table[key] = "-" #문자로 지정
        table[key] = 1  # 숫자로 지정
    else:
        # 존재
        #table[key] = table[key] + "-"
        table[key] = table[key] + 1

# 출력하기. 딕셔너리 key와 값이 쌍으로 열거. items( )
for item in table.items():
    print("items >>> ", item[0], item[1])


for item in table.items():
    print(item[0], item[1], item[0]*item[1])

# 1. 파일 저장 할 때 utf-8 인코딩을 설정하시오.
# 2. 실행하면 줄바꿈이 안된다. 어떻게 처리할까?
# 3. 파일이 없으면 쓰기 모드로 파일을 얻는 코드를 추가하시오.

# phones.txt 파일에 아래의 2줄 쓰고 저장하시오.
# 최무선  010-1111-2222
# 정중부  010-2222-3333

outfile = open("phones.txt", "a")

outfile.write("최무선 010-1111-2222")
outfile.write("정충부 010-2222-3333")

outfile.close()

# 기존의 phones.txt 파일에 위에 2줄을 추가 저장 할때는 
# 위처럼 코딩을 하고 파일처리에 terminal 를 하고 
# python .\phones.txt 를 선택하면 추가된다. 
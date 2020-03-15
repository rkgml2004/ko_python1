
#  proverbs.txt 파일에서 줄 단위로 읽어서 output.txt 에 쓰시오 
 pfr = open("./file/proverbs.txt", "r")
 
outfile = open("proverbs.txt", "w")

if os.path.isfile("proverbs.txt"):
    print("동일한 이름의 파일이 이미 존재합니다. ")
else:
    outfile.write("")
    outfile.write("")
    outfile.write("")

outfile.close()
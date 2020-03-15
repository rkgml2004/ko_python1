# GUI 모듈
#  turtle
#  tkinter > 리눅스 tk / tcl 언어를 파이썬으로 표현

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askopenfilename

readFile = askopenfilename()  # 절대 경로 표시되는 파일명,

if (readFile != None):
    infile = open(readFile, "r")

for line in infile.readlines():
    line = line.strip()
    print(line)

infile.close()


def main():
    # 파일의 존재여부 체크
    if readFile != None:
        # 파일열기
        infile = open(readFile, "r", encoding="UTF-8")
        # 파일처리
        for line in infile.readlines():
            line = line.strip()  # .strip ( ) 양쪽에 공백 제거.
            print(line)  # 표준(모니터) 출력

        # 파일닫기
        infile.close()
     else:
        print("파일 없음")
if __name__ == "__main__":

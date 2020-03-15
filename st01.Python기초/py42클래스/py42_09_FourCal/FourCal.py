
# 작업 순서
# 1. 모듈 또는 클래스 import
# 2. 클래스명은 파스칼 표기법으로 정한다. 첫글자는 대문자로.
#     생성자 선언 : 인스턴스가 생성될 때 실행
#     소멸자 선언 : 소멸자는 인스턴스가 소멸할 때 실행
#     __str__() 메서드 오버라이딩
#     접근자( getter ) 메서드 선언. 비공개 인스턴스 변수 읽기
#     설정자( setter ) 메서드 선언. 비공개 인스턴스 변수 수정
#     사용자 메서스 선언
# 3. main() 메서드 만들기
#     인스턴스 생성
# 4. 이 모듈이 단독으로 사용되면 main()를 호출하라.
#    if __name__ == "__main__":
#    main()


# 코딩 하기
# gene 코딩
class Gene:
    def __init__(self, creationid, creationseq):
        print("I'm a new Gene object!")
        print("My constructor got a param : " + str(creationid))
        print("Assigning that param to my in instance variable...")
        self.id = creationid
        print("Similarly, assigning to my sequence instance variable...")
        self.sequence = creationseq

    def print_id(self):
        print("My id is : " + str(self.id))

    def print_len(self):
        print("My sequence len is : " + str(len(self.sequence)))


print("\n***       Creating geneA:")
geneA = Gene("AY342", "CATTGAC")

print("\n***       Creating geneB: ")
geneB = Gene("G54B", "GGTCTCAAAT")

print("\n***       Asking geneA to print_id() : ")
geneA.print_id()

print("\n***       Asking geneB to print_id() : ")
geneB.print_id()

print("\n***       Asking geneA to print_len() : ")
geneA.print_len()

print("\n***       Asking geneB to print_len() : ")
geneB.print_len()


def base_composition(self, base):
    base_count = 0
    for index in range(0, len(self.sequence)):
        base_i = self.sequence[index]
        if base_i == base:
            base_count = base_count + 1
    return base_count


def gc_content(self):
    g_count = self.base_composition("G")
    c_count = self.base_composition("C")
    return (g_count + c_count)/float(len(self.sequence))


print("\n***       Asking geneA to return its T content : ")
geneA_t = geneA.base_composition("T")
print(geneA_t)

print("\n***       Asking geneA to return its GC content : ")
geneA_gc = geneA.gc_content()
print(geneA_gc)


def get_seq(self):
    return self.sequence


def set_seq(self, newseq):
    self.sequence = newseq


def set_seq(self, newseq):
    if newseq.base_composition("U") != 0:
        print("Sorry, no RNA allowed.")
    else:
        self.sequence = newseq


def set_seq(self, newseq):
    assert newseq.base_composition("U") == 0, "Sorry, no RNA allowed."
    self.sequence = newseq


print("***     Creating geneA: ")
geneA = Gene("AY342", "CATTGAC")

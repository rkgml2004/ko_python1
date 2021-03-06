
# 작업 순서
# 1. 모듈 또는 클래스 import
# 2. Parent 부모 클래스를 선언합니다.
# 3. Child 자식 클래스를 선언합니다. 부모 자식 관계 설정 하는 것이 중요.
# 4. main() 메서드 만들기
#     자식 클래스의 인스턴스를 생성하고 부모의 메서드를 호출합니다.
# 5. 이 모듈이 단독으로 사용되면 main()를 호출하라.
#    if __name__ == "__main__":
#    main()


# 코딩 하기
# parent 클래스 만들기
class Parent():
    def __init__(self):
        self.value = "부모 변수"

    def test(self):
        print("Parent 클래스의 test( ) 매서드 입니다.")

    def getValue(self):
        return self.value

# child 클래스 만들기


class Child (Parent):
    def __init__(self): "자식 변수"
    pass


child = Child()
child.test()
val = child.getValue()
print(val)  # "부모 변수"

# class child( 빈칸에 부모를 넣어주면 됨).

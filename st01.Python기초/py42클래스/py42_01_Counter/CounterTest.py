
# 작업 순서
# 1. 모듈 또는 클래스 import
# 2. main() 메서드 만들기
#     인스턴스 생성
# 3. 이 모듈이 단독으로 사용되면 main()를 호출하라.
#    if __name__ == "__main__":
#    main()

# 코딩 하기
# counter 클래스명 import

import Counter


def main():
    isinstance1 = Counter.counter()  # counter 인스턴스 생성
    print(instance1.__str__())

    instance1.increment()
    instance1.increment()

    curval = instance1 .getCounter()
    print("curval", curval)
    print(instance1.__str__())


if __name__ == "__main__":
    main()

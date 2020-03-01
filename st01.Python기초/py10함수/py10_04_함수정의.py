
# 내장함수

# 사용자함수


n = int(input("정수를 입력하시오."))
i = 1


def isprime(n):
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True


print(isprime(n))

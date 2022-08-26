"""
1. brute force의 무차별 대입
2. 제곱근
3. femat's little theorem
P가 소수이고 a가 P의 배수가 아닐 경우 a^P-1 = 1(mod P)이다.
즉 a^P-1로 나눈 나머지는 1이다.
"""
import math
import random
import time


def test_finding_prime(number):
    num = abs(number)
    if num < 4: return True
    for x in range(2, num):
        if num % x == 0:  # 나누어 떨어지는 게 있으면 소수가 아니다
            return False
    return True


def test_finding_prime_sqrt(number):
    num = abs(number)  # 절대값
    if num < 4: return True  # 4미만은 전부 소수
    for x in range(2, int(math.sqrt(num)) + 1):  # 제곱근까지만 for
        if number % x == 0:
            return False


# a^P-1로 나눈 나머지가 1이면 P는 소수다
def test_finding_prime_fermat(number):
    if number <= 102:
        for a in range(2, number):
            if pow(a, number - 1, number) != 1:
                return False
        return True
    else:
        for i in range(100):
            a = random.randint(2, number - 1)
            if pow(a, number - 1, number):
                return False
        return True


if __name__ == '__main__':
    start = time.process_time()
    number1 = 17
    number2 = 40000
    assert (test_finding_prime_fermat(number1)is True)
    assert (test_finding_prime_fermat(number2) is False)
    print(f"Time elapsed : {time.process_time() - start}") # 초 단위로 프린트됨

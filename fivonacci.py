"""
generator 함수는 yield를 사용한다.
next가 실행될 때 마다 yield b++

전체 시퀀스를 한 번에 메모리에 생성
정렬 필요 없음
generator순회 할 때마다 마지막으로 호출된 효소를 기억하고 다음 값을 반환한다
"""


def fib_generator():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


if __name__ == '__main__':
    fib = fib_generator()
    for _ in range(10):
        print(next(fib), end=" ")

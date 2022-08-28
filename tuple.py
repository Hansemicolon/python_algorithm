"""
시퀀스 언패킹 연산자 *
모든 반복 가능한 객체([],{},() 등)에 사용하여 언패킹 가능

파이선 표준 모듈 collections 에는 네임드 튜플이라는 시퀀스 데이터 타입이 있다
튜플 항목에 인덱스 위치뿐만이 아니라 이름으로도 참조할 수 있다.
"""
import time


def tuple_unpaking():
    x, *y = (1, 2, 3, 4)
    print(x, y)  # x=1, y=[2, 3, 4]
    *x, y = (1, 2, 3, 4)
    print(x, y)  # x=[1, 2, 3], y=4
    x, y, *z = (1, 2, 3, 4)
    print(x, y, z)  # x=1 y=2 z=[3, 4]


def named_tuple():
    import collections
    # field를 공백으로 구분된 문자열로 지정한다ㅋㅎ
    Stomi = collections.namedtuple('Stomi', 'name age gender')  # typename: stomi, filed: name, age, gender
    Stomi.name = "한세미"
    s = Stomi(name="한세미", age=20, gender='여')
    print(s)  # Stomi(name='한세미', age=20, gender='여')
    print(s.age)  # 20
    s.name = "숨통희"
    print(s.name)  # Error 일반 튜플과 마찬가지로 불변형이다.

if __name__ == '__main__':
    tuple_unpaking()
    named_tuple()
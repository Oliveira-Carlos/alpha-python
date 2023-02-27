from typing import Generator


def count_up(x: int) -> Generator[int, None, None]:

    a = 1
    b = 1
    while b < x:
        a, b = b, b + (b - a + 1)
        yield a


user_number = int(input("type a integer"))

for i in count_up(user_number):
    print(i)

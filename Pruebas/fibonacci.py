"""Hacer un programa que de los numeros de la secuencia de fibonacci"""

import sys
import time
from typing import Callable


def fibonnacci(maximus: int) -> list[int]:
    a, b = 0, 1
    lista_fibonacci = list([0])
    for i in range(maximus):
        if b > maximus:
            return lista_fibonacci
        else:
            lista_fibonacci.append(b)
            a, b = b, a + b


optimized_fib: Callable[..., int] = lambda n, a=0, b=1, res=[]: (
    res if b > n else optimized_fib(n, b, a + b, res + [b])
)


def main(*args: None) -> int:
    start1 = time.time()

    optimized_fib()

    end1 = time.time()
    start2 = time.time()

    fibonnacci()

    end2 = time.time()

    print(f"Optimized fib: {end1-start1}")
    print(f"fib: {end2-start2}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

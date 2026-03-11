#!/usr/bin/python3
import sys


def factorial(n):
    """Calculate the factorial of a non-negative integer recursively.

    Function Description:
        Computes the factorial of ``n`` by multiplying ``n`` by the
        factorial of ``n - 1`` until reaching the base case.

    Parameters:
        n (int): The non-negative integer whose factorial is computed.

    Returns:
        int: The factorial of ``n``.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


f = factorial(int(sys.argv[1]))
print(f)
#!/usr/bin/python3
"""
Minimum Operations
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.

    Parameters:
    n (int): The target number of H characters.

    Returns:
    int: The minimum number of operations needed, or 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations

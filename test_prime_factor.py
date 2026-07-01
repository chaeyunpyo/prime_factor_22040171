import pytest

from prime_factor import PrimeFactor

def test_prime_factor_of_1():
    prime_factor = PrimeFactor()
    assert prime_factor.factorial(1) == []

def test_prime_factor_of_2():
    prime_factor = PrimeFactor()
    assert prime_factor.factorial(2) == [2]

def test_prime_factor_of_3():
    prime_factor = PrimeFactor()
    assert prime_factor.factorial(3) == [3]
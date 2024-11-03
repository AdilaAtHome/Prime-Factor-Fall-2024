# test module for assignment 3: Generate a list of the prime numbers for a given number
import pytest
import prime


# Step #1: test asserts that a value that is not an integer raises a ValueError
def test_not_an_integer():
    with pytest.raises(ValueError):
        prime.generate_prime_factors("NotAnInteger")




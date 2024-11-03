"""
Assignment 3: Module containing function to generate prime factors list
"""


# Function creates list of prime factors for a value
def generate_prime_factors(value):
    # Raises a Value Error if the value is not an integer
    if not isinstance(value, int):
        raise ValueError(f'{value} is not an integer.')

def sum_a_tuple(*numbers):
    total = sum(numbers)
    return total


# Tuple of integers
print(sum_a_tuple(1, 2, 3, 4, 5))
# Tuple of floats
print(sum_a_tuple(1.5, 2.7, 3.2, 4.8))
# Empty tuple
print(sum_a_tuple())
# Tuple with negative numbers
print(sum_a_tuple(-1, -2, -3, -4, -5))

'''
Given an array of integers, find the first missing positive integer in linear
time and constant space. In other words, find the lowest positive integer that
does not exist in the array. The array can contain duplicates and negative
numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should
give 3.

You can modify the input array in-place.
'''


def first_missing(numbers):
    missing = 1
    for n in numbers:
        missing += 1 if n == missing else 0
    return missing

# Testing
assert first_missing([3, 4, -1, 1]) == 2
assert first_missing([1, 2, 0]) == 3
assert first_missing([]) == 1

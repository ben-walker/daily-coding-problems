'''
Given an array of integers, return a new array such that each element at index
i of the new array is the product of all the numbers in the original array
except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would
be [2, 3, 6].

Follow-up: what if you can't use division?
'''

from functools import reduce
from operator import mul


def productify_list(rawList):
    productified = []
    for i in range(len(rawList)):
        productified.append(reduce(mul, rawList[:i] + rawList[i + 1:]))
    return productified

# Testing
assert productify_list([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert productify_list([]) == []
assert productify_list([3, 2, 1]) == [2, 3, 6]
assert productify_list([0, 1, 2, 3, 4, 5, 6]) == [720, 0, 0, 0, 0, 0, 0]

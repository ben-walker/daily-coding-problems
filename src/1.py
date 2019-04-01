'''
Given a list of numbers and a number k, return whether any two numbers from
the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''


def add_to_k(numbers, k):
    tracker = []
    for n in numbers:
        if n in tracker:
            return True
        tracker.append(k - n)
    return False

# Testing
assert add_to_k([10, 15, 3, 7], 17)
assert not add_to_k([], 17)
assert not add_to_k([17], 17)
assert add_to_k([17, 0], 17)
assert add_to_k([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 17)
assert add_to_k([0, 0], 0)
assert add_to_k([15, 2, 3, 0, -1, 2, 3, -5], -6)
assert not add_to_k([0], 0)

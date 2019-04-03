'''
Given a list of integers, write a function that returns the largest sum of
non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''


def largest_non_adjacent_sum(numbers):
    incl = numbers[0]
    excl = 0

    for n in numbers[1:]:
        new_excl = max(incl, excl)
        incl = excl + n
        excl = new_excl

    return max(incl, excl)

assert largest_non_adjacent_sum([2, 4, 6, 2, 5]) == 13
assert largest_non_adjacent_sum([5, 1, 1, 5]) == 10

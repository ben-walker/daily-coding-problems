'''
Given an array of time intervals (start, end) for classroom lectures (possibly
overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''


def end_time(interval):
    return interval[1]


def min_rooms(lec_times):
    chrono_lec_times = sorted(lec_times, key=lambda i: end_time(i))
    overlapping_rooms = [chrono_lec_times.pop(0)]
    max_room_intersect = 0

    for interval in chrono_lec_times:
        start, end = interval
        while overlapping_rooms and end_time(overlapping_rooms[0]) < start:
            overlapping_rooms.pop(0)
        overlapping_rooms.append(interval)
        max_room_intersect = max(max_room_intersect, len(overlapping_rooms))
    return max_room_intersect

# Testing
assert min_rooms([(30, 75), (0, 50), (60, 150)]) == 2
assert min_rooms([(0, 50), (30, 75), (60, 150), (10, 87), (100, 120), (40, 80),
                 (150, 200)]) == 4

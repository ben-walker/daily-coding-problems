'''
Given an unordered list of flights taken by someone, each represented as
(origin, destination) pairs, and a starting airport, compute the person's
itinerary. If no such itinerary exists, return null. If there are multiple
possible itineraries, return the lexicographically smallest one. All flights
must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'),
('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return
the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting
airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and
starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'].
'''


def find_itinerary(flights, start):
    itinerary = []

    while start:
        itinerary.append(start)
        next_flight = next((v for i, v in enumerate(flights) if
                            v[0] == start), None)
        start = next_flight[1] if next_flight else None
        if next_flight:
            flights.remove(next_flight)
    return itinerary if not len(flights) else None

assert find_itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'),
                      ('HKO', 'ORD')], 'YUL') == ['YUL', 'YYZ', 'SFO', 'HKO',
                                                  'ORD']
assert find_itinerary([('SFO', 'COM'), ('COM', 'YYZ')], 'COM') is None
assert find_itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A') \
    == ['A', 'B', 'C', 'A', 'C']

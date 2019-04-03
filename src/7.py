'''
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as
'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not
allowed.
'''

valid_codes = [str(x) for x in range(1, 27)]


def decodings(msg):
    if not msg:
        return 1

    count = 0
    for code in valid_codes:
        if msg.startswith(code):
            count += decodings(msg.replace(code, '', 1))
    return count

# Testing
assert decodings('1111111128') == 55
assert decodings('111') == 3
assert decodings('') == 1
assert decodings('99999999') == 1
assert decodings('1219') == 5

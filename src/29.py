'''
Run-length encoding is a fast and simple method of encoding strings. The basic
idea is to represent repeated successive characters as a single count and
character. For example, the string "AAAABBBCCDAA" would be encoded as
"4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be
encoded have no digits and consists solely of alphabetic characters. You can
assume the string to be decoded is valid.
'''


def run_len_encode(string):
    tab = 1
    tracker = ''

    for i, c in enumerate(string[1:], 1):
        if c == string[i - 1]:
            tab += 1
        else:
            tracker += f'{tab}{string[i - 1]}'
            tab = 1
    return tracker + f'{tab}{string[i - 1]}'

# Testing
assert run_len_encode('AAAABBBCCDAA') == '4A3B2C1D2A'

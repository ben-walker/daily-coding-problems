'''
Given a dictionary of words and a string made up of those words (no spaces),
return the original sentence in a list. If there is more than one possible
reconstruction, return any of them. If there is no possible reconstruction,
then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the
string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the
string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or
['bedbath', 'and', 'beyond'].
'''


def listify(sentence, dictionary):
    word_builder = []
    original_sentence = []

    for char in sentence:
        word_builder.append(char)
        word = ''.join(word_builder)
        if word in dictionary:
            original_sentence.append(word)
            word_builder.clear()
    return None if not original_sentence else original_sentence

# Testing
sentence = listify('thequickbrownfox', ['quick', 'brown', 'the', 'fox'])
assert sentence == ['the', 'quick', 'brown', 'fox']
sentence = listify('bedbathandbeyond', ['bed', 'bath', 'bedbath', 'and',
                                        'beyond'])
assert sentence == ['bed', 'bath', 'and', 'beyond']

# also this is a crap solution

"""

everse the order of words in a given string sentence. You can assume that sentence does not have any leading, trailing or repeating spaces.

Example

For sentence = "Man bites dog", the output should be
solution(sentence) = "dog bites Man".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string sentence

A string consisting of letters and spaces.

Guaranteed constraints:
1 ≤ sentence.length ≤ 2 · 104.

[output] string
"""

def solution(sentence):
    sentence = sentence.split(" ")
    print(sentence)
    return ' '.join(reversed(sentence))


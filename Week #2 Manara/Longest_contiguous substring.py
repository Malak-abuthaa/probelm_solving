"""

Given a string of lowercase English letters, find the length of its longest contiguous substring that doesn't contain any character more than once.

Example

For s = "abcabba", the output should be
solution(s) = 3.

The longest substring with unique characters is abc, so the answer should be 3.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

A string containing only lowercase English letters.

Guaranteed constraints:
3 ≤ s.length ≤ 106.

[output] integer
"""


def solution(s):
    res = 0
    c = ""

    for i in range(len(s)):
        print("c", c)
        print("res", res)

        if s[i] not in c:
            c += s[i]
        else:
            res = max(res, len(c))
            # remove the the doublicate char in x
            c = c[c.index(s[i]) + 1:] + s[i]

    return max(res, len(c))


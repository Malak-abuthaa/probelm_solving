"""
remove adjacent duplicate characters.

Example

For s = "aaaaa", the output should be
solution(s) = "a";
For s = "abccaaab", the output should be
solution(s) = "abcab".
Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

A string containing lowercase English letters only.

Guaranteed constraints:
0 ≤ s.length ≤ 106.

[output] string

A new string with adjacent duplicates removed.


"""


def solution(s):
    p1 = 0
    p2 = 1

    while p2 < len(s):

        if s[p1] == s[p2]:
            s = s[:p1] + s[p2:]
        else:
            p1 += 1
            p2 += 1

    return s


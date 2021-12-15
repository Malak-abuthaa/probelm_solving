"""
time = O(N log N)
space = O(1)
Given a list of sorted characters letters containing only lowercase letters, and given a target letter, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"
"""


def solution(letters, target):
    if letters[0] > target or letters[-1] <= target:
        return letters[0]
    l = 0
    h = len(letters) - 1
    while l <= h:
        m = l + (h - l) // 2
        if letters[m] <= target:
            l = m + 1
        elif letters[m] > target:
            h = m - 1
    return letters[l]

"""Given two arrays, write a function to compute their intersection.

Example 1:

Input: arr1 = [1,2,2,1], arr2 = [2,2]
Output: [2]
Example 2:

Input: arr1 = [4,9,5], arr2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result must be in the same order as in arr2
[execution time limit] 4 seconds (py3)

[input] array.integer arr1

[input] array.integer arr2

[output] array.integer

[Python 3] Syntax Tips"""
"""
Time = O( n + m )
space  = O( n)

"""


def solution(arr1, arr2):
    mapping = {}
    for num in arr1:
        mapping[num] = 0

    arr1 = []

    for num in arr2:
        if num in mapping:
            arr1.append(num)
            mapping.pop(num)

    return arr1



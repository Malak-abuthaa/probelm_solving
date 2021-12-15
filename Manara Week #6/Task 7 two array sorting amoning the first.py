""""
Time = O( a + b + b^2)
space = O(b)


Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

Constraints:

arr1.length, arr2.length <= 100
0 <= arr1[i], arr2[i] <= 1000
Each arr2[i] is distinct.
Each arr2[i] is in arr1.
[execution time limit] 4 seconds (py3)

[input] array.integer arr1

[input] array.integer arr2

[output] array.integer
"""


def solution(arr1, arr2):
    d = {}

    for i in range(len(arr1)):
        if arr1[i] in d:
            d[arr1[i]] = d[arr1[i]] + 1
        else:
            d[arr1[i]] = 1

    res = []
    for item in arr2:
        if item in d:
            for i in range(d[item]):
                res.append(item)
            del d[item]
    arr2 = sorted(d.keys())
    for item in arr2:
        for i in range(d[item]):
            res.append(item)

    return res




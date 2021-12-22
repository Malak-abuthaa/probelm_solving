"""Implement Merge Sort using your preferred programming language"""
""""
time  = O(n log n)
space = ON)
"""

def merge(arr1, arr2):
    res = []
    while len(arr1) != 0 and len(arr2) != 0:
        if arr1[0] < arr2[0]:
            res.append(arr1[0])
            arr1.remove(arr1[0])
        else:
            res.append(arr2[0])
            arr2.remove(arr2[0])
    if len(arr1) == 0:
        res += arr2
    else:
        res += arr1
    return res


def mergeSort(x):
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x) // 2
        a = mergeSort(x[:middle])
        b = mergeSort(x[middle:])
        return merge(a, b)


print(mergeSort([1, 5, 7, 6, 5, 4, 8, 44, 50]))




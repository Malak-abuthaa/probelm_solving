# import requests
# import mysql.connector
# import pandas as pd

"""eathir done ny heap or qiouck sort, but we dont garantee that quick sort are stable in term of time
"""
import heapq


def sort_by_heap(nums):
    heapq.heapify(nums)
    return nums


## using quick sort
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


arr = [5, 8, 1, 4, 6, 8]
quickSort(arr, 0, 5)

print(arr)


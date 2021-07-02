# import requests
# import mysql.connector
# import pandas as pd

def binery_search(arr, low, high, val):
    mid = (low + high) // 2

    if (val == arr[mid]):
        return mid
    elif arr[mid] > val:
        return binery_search(arr, low, mid - 1, val)
    else:
        return binery_search(arr, mid + 1, high, val)
    return -1


print(binery_search([2, 5, 6, 7, 8, 9], 0, 5, 5))

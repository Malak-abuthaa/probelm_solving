def searchIndex(arr, val):
    if val > arr[len(arr) - 1]:
        return len(arr)
    elif val < arr[0]:
        return 0

    for i in range(len(arr) - 1):
        if val >= arr[i] and val <= arr[i + 1]:
            return i + 1

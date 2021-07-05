def findIntersection(arr1, arr2):
    mapping = {}
    for num in arr1:
        mapping[num] = 0

    arr1 = []

    for num in arr2:
        if num in mapping:
            arr1.append(num)
            mapping.pop(num)

    return arr1


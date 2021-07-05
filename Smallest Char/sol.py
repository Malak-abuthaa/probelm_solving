def smallestCharacter(letters, target):
    if target >= letters[-1]:
        return letters[0]

    l = 0
    r = len(letters) - 1
    while l < r:
        mid = (l + r) // 2
        if letters[mid] <= target:
            l = mid + 1
        else:
            r = mid
    return letters[l]






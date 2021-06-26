def countPairsWithDifference(k, a):
    numbers = {}

    for num in a:
        if num in numbers:
            numbers[num] = numbers[num] + 1
        else:
            numbers[num] = 0

    counter = 0
    for num in a:
        if (num - k) in numbers and (numbers[num] > -1 or numbers[(num - k)] > -1):
            print(num, (num - k))
            numbers[num] = numbers[num] - 1
            numbers[abs(k - num)] = numbers[abs(k - num)] - 1
            counter += 1
    print(numbers)

    return counter


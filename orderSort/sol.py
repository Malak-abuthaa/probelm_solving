def orderSort(arr1, arr2):
    part_one = []
    part_two = []
    arr2_dict = {}
    for num in range(len(arr2)):
        arr2_dict[arr2[num]] = num
    index = 0
    for num in arr1:
        if num in arr2_dict:
            part_one.append(num)
        else:
            part_two.append(num)

    return sorted(part_one, key=lambda x: arr2_dict[x]) + sorted(part_two)

##anther sol


counting={}
result=[]
nomatch=[]

    for num in arr1:
        if num not in counting:
            counting[num]=1
        else:
            counting[num]+=1


    for num in arr2:
        result.extend([num]*counting[num])
        del counting[num]


    for num in counting:
        nomatch.extend([num]*counting[num])

    nomatch.sort()
    return result+nomatch
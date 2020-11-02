def TwoSumIndicesHashMap(array , targetSum):
    NewDict = {}
    for num in array:
        num1 = targetSum - num
        if num1 in NewDict:
            NewDict[num] = array.index(num)
            return [NewDict[num1],NewDict[num]]
        else:
            NewDict[num] = array.index(num)

    return []

array = [5,6,1,8,-6,11,-1]
target = -5
print(TwoSumIndicesHashMap(array , target))

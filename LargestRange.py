def largestRange(array):
    dupHash = {}
    largeArray = []
    longValue = 0
    for i in array:
        dupHash[i] = True
    for i in array:
        if not dupHash[i]:
            continue
        dupHash[i] = False
        currentValue = 1
        left = i-1
        right = i+1
        while left in dupHash:
            dupHash[left] = False
            currentValue += 1
            left -= 1
        while right in dupHash:
            dupHash[right] = False
            currentValue += 1
            right += 1
        if currentValue > longValue:
            longValue = currentValue
            largeArray = [left+1, right-1]
    return largeArray

#time complexity is o(n) and space complexity is o(n)
array = [1,11,5, 3, 4, 8, 7, 2, 0, 6, 12, 14 , 15 , 20]
print(largestRange(array))

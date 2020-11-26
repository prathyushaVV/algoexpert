#this ia bad approach as it has o(nlogn)and O(n) time and space complexity

def subarraySort(array):
    arr = sorted(array)
    print(arr)
    unsorted = []
    res =[]
    for i in range(1,len(array)-1):
        if array[i] < array[i-1] or array[i] > array[i+1]:
            unsorted.append(array[i])

    mini = min(unsorted)
    maxi = max(unsorted)

    for i in range(len(arr)):
        if arr[i] == maxi :
            res.append(i)
            maxi = float("inf")
        if arr[i] == mini:
            res.append(i)
            mini = fl
    return res

array = [1,2,4,7,10,11,7,12,6,7,16,18,19]
print(subarraySort(array))

def subarraySOrting(array):
    minout = float("inf")
    maxout = float("-inf")
    for i in range(len(array)):
        num = array[i]
        if isOutOfOrder(i, num, array):
            minout = min(minout, num)
            maxout = max(maxout , num)

        if minout == float("inf"):
            return [-1,-1]

    shortLeftIndex = 0
    while minout >= array[shortLeftIndex]:
        shortLeftIndex += 1
    shortRightIndex = len(array) - 1
    while maxout <= array[shortRightIndex]:
        shortRightIndex -= 1

    return [shortLeftIndex, shortRightIndex]

def isOutOfOrder(i, num, array):
    if i == 0:
        return num > array[i+1]
    if i == len(array):
        return num < array[i-1]
    return num > arr[i+1] or num < arr[i-1]



#things which r imp
#find all the unsorted numbers
#if one unsorted num is present then there will the atleast 2 unsorted numbers
#and need to find the smllaest and greatest and there final positions after sorting

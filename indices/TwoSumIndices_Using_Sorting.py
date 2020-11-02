#time complexity = O(nlogn) space compleity is O(n)
def TwoSumIndices(array , target):
    arr = sorted(array)
    left = 0
    right = len(arr)-1
    print(arr, left , right, array)
    idx = []
    while left < right:
        val = arr[left] + arr[right]
        if val < target:
            left += 1
        elif val > target:
            right -= 1
        else:
            firstNum = arr[left]
            secondNum = arr[right]
            break
    for i in range(len(array)):
        if array[i] == firstNum or array[i] == secondNum:
            idx.append(i)
    return idx

array = [5,6,1,8,-6,11,-1]
target = -5
print(TwoSumIndices(array , target))

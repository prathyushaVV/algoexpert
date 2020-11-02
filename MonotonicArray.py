def isMonotonic(array):
    isAscending = True
    isDesending = True
    for i in range(1,len(array)):
        if array[i] < array[i-1]:
            isAscending = False
        if array[i] > array[i-1]:
            isDesending = False
    return isDesending or isAscending


array = [-1,-5,-1100,-1100,-1101,-1103,-9901]
print(isMonotonic(array))


#monotonic array means array should be either non decreasing or non increasing
#non deacreasing includes incresing and equals values are also allowed
#if we have to find the strictly decreasing or increasing we should have all unique values

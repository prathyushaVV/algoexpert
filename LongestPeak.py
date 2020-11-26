def longestPeak(array):
    ActCount = 0
    CurCunt = 0
    for i in range(1, len(array)-1):
        if array[i] > array[i-1] and array[i] > array[i+1]:
            CurCunt = CurCunt + 3
            for l in reversed(range(1,i)):
                if array[l] <= array[l-1]:
                    break
                else:
                    CurCunt += 1
            for j in range(i+1, len(array)-1):
                if array[j] <= array[j+1]:
                    break
                else:
                    CurCunt += 1
            ActCount = max(ActCount, CurCunt)
            CurCunt = 0
    return ActCount

array = [1,2,3,3,4,0,10,6,5,-1,-3,2,3]
print(longestPeak(array))

#there are two peaks
#4 is one peak and 10 ia longestPeak
#4 peaks length is 3, 4, 0 which is 3
#10 peak has 0,10,6,5,-1,-3 where the length is 6

def LongPeakEx(array):
    longestpeak = 0
    currentPeak = 0
    i = 0
    while i < len(array):
        if array[i] < array[i-1] or array[i] < arra[i+1]:
            

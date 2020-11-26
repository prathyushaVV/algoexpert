arr = [-10, -5, -3, 1, 2, 6, 9]

sqrr = [0, 0, 0, 0, 0, 0, 0]

i = 0
j = len(arr)-1
k = len(arr)-1
while i < j:
    if(abs(arr[i]) < abs(arr[j]) ):
        sqrr[k] = arr[j]*arr[j]
        j -= 1
        k -= 1
    if(abs(arr[i]) > abs(arr[j])):
        sqrr[k] = arr[i]*arr[i]
        i += 1
        k -= 1
    else:
        sqrr[k] = arr[i]*arr[i]
        

print(sqrr)

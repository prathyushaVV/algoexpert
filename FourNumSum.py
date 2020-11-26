#time complexity is O(n2) worst case has O(n3) space is O(n2)
def FourNumSum(array, targetNum):
    duplets = {}
    quadruplets = []
    for i in range(1, len(array)-1):
        for j in range(i+1, len(array)):
            total = array[i] + array[j]
            diff = targetNum - total
            if diff in duplets:
                for pair in duplets[diff]:
                    quadruplets.append(pair + [array[i],array[j]])
            #total = 0
        for k in range(0,i):
            total2 = array[k] + array[i]
            if total2 not in duplets:
                duplets[total2] = [[array[i], array[k]]]
            else:
                duplets[total2].append([array[i],array[k]])
            #total2 = 0
    return quadruplets

array = [7,6,4,-1,1,2]
targetNum = 16
print(FourNumSum(array,targetNum))

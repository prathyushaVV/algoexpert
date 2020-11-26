
def hourGlass(array):
    totalSum = 0
    highestSum = 0
    for i in range(len(array)-2):
        for j in range(len(array)-2):
            totalSum = array[i][j] + array[i][j+1] + array[i][j+2] + array[i+1][j+1] + array[i+2][j] +array[i+2][j+1] + array[i+2][j+2]
            if highestSum < totalSum:
                highestSum = totalSum
    return highestSum

array = [[-9 ,-9, -9,  1, 1, 1], [0 ,-9 , 0 , 4, 3, 2],[-9, -9, -9 , 1, 2, 3],[0,  0,  8,  6 ,6, 0],[0,  0,  0 ,-2, 0, 0],[0,  0,  1,  2, 4, 0]]
print(hourGlass(array))

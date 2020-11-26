def SprialTraverse(matrix):
    sc = 0
    ec = len(matrix[0])-1
    sr =0
    er = len(matrix)-1
    res = []
    while sr <= er and sc <= ec:
        for col in range(sc,ec):
            res.append(matrix[sr][col])
        for row in range(sr+1,er+1):
            res.append(matrix[row][ec])
        for col in reversed(range(sc,ec)):
            res.append(matrix[er][col])
        for row in reversed(range(sr+1,er)):
            res.append(matrix[row][sc])
        sr += 1
        er -= 1
        sc += 1
        ec -= 1
    return res



def SpiralTraverseRecursive(matrix):
    res = []
    spiralFill(matrix, 0, len(matrix)-1, 0, len(matrix[0])-1, res)
    return res

def spiralFill(matrix, sr, er, sc, ec, res):
    if sr > er or sc > ec:
        return
    for col in range(sc,ec):
        res.append(matrix[sr][col])
    for row in range(sr+1,er+1):
        res.append(matrix[row][ec])
    for col in reversed(range(sc,ec)):
        res.append(matrix[er][col])
    for row in reversed(range(sr+1,er)):
        res.append(matrix[row][sc])

    spiralFill(matrix, sr+1,er-1,sc+1,ec-1,res)


array = [[-9 ,-9, -9,  1, 1, 1], [0 ,-9 , 0 , 4, 3, 2],[-9, -9, -9 , 1, 2, 3],[0,  0,  8,  6 ,6, 0],[0,  0,  0 ,-2, 0, 0],[0,  0,  1,  2, 4, 0]]
print(SpiralTraverseRecursive(array))

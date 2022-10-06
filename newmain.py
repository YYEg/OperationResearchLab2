import numpy as np


def VectorChange(matrix, row, col):
    cj = list(matrix[0][:-1]) #Список значений целевой функции
    sum = 0
    sumArr = []
    for i in range(0, col - 1):
        for j in range(1, row):
            sum += matrix[j][i]
        sumArr.append(sum)
        sum = 0
    jcj = []
    for z in range(len(sumArr)):
        for j in range(4):
            if sumArr[z] == 1.0:
                jcj[j] = cj[z]

    for i in (1,col - 1):
        for j in range(1,row - 1):
            deltaJ = matrix[i][j]
matrix = np.loadtxt("data.txt", dtype=float)
(row, col) = matrix.shape
basisVectors = list(range((col) - (row - 1), col))
VectorChange(matrix, row, col)
print(1)
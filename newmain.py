import numpy as np


def VectorChange(matrix, row, col):
    cj = list(matrix[0][:9]) #Список значений целевой функции
    sum = 0
    sumArr = [] #массив сумм значений в матрице
    for i in range(0, col - 1):
        for j in range(1, row):
            sum += matrix[j][i]
        sumArr.append(sum)
        sum = 0
    jcj = [] #массив значений целевых функций базисных векторов
    for i in range(len(sumArr)):
        if sumArr[i] == 1.0:
            jcj.append(cj[i])

    deltaJ = [] #массив дельта жи
    deltaSum = 0
    test = []
    for i in range(0, col):
        for j in range(len(jcj)):
            deltaSum += (matrix[j][i] * jcj[j])
            test.append(deltaSum)
        deltaSum -= cj[i]
        deltaJ.append(deltaSum)
        deltaSum = 0
    jnum = deltaJ.index(min(deltaJ)) #вносимый вектор
    m = []
    for i in range(row):
        if matrix[i][jnum] == 0:
            m.append(0)
        else:
            m.append(matrix[i][-1] / matrix[i][jnum])
    inum = m.index(min([x for x in m[1:] if x != 0]))  # Перенести нижний индекс
    basisVectors[inum - 1] = jnum
    r = matrix[inum][jnum]
    matrix[inum] /= r
    for i in [x for x in range(row) if x != inum]:
        r = matrix[i][jnum]
        matrix[i] -= r * matrix[inum]
def solve(matrix, row, col):
    flag = True
    while flag:
        if max(list(matrix[0][:-1])) <= 0: # Пока все коэффициенты не будут меньше или равны 0
            flag = False
        else:
            VectorChange(matrix, row, col)
def printSol(matrix, col):
    for i in range(col - 1):
        if i in basisVectors:
            print("x"+str(i)+"=%.2f" % matrix[basisVectors.index(i)+1][-1])
        else:
            print("x"+str(i)+"=0.00")
    print("objective is %.2f"%(-matrix[0][-1]))
matrix = np.loadtxt("newdata.txt", dtype=float)
(row, col) = matrix.shape
basisVectors = list(range((col) - (row - 1), col))
VectorChange(matrix, row, col)
solve(matrix, row, col)
printSol(matrix, col)
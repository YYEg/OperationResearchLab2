import numpy as np
def VectorChange(matrix, row, col):
    print("Ваша текущая матрица")
    print('\n'.join([''.join(['{:25}'.format(x) for x in row])
                     for row in matrix]))
    print()

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
    for i in range(0, col):
        for j in range(len(jcj)):
            deltaSum += (matrix[j][i] * jcj[j])
        deltaSum -= cj[i]
        deltaJ.append(deltaSum)
        deltaSum = 0
    jnum = deltaJ.index(min(deltaJ[:-1])) #вносимый вектор

    m = [] #массив для поиска минимального значения
    for i in range(row):
        if matrix[i][jnum] == 0:
            m.append(0)
        else:
            m.append(matrix[i][-1] / matrix[i][jnum])

    inum = m.index(min([x for x in m[1:] if x > 0 ]))  # Минимальное значение выводится из базиса
    basisVectors[inum - 1] = jnum #[inum - 1] для того чтобы убрать первый в массиве член, принадлежащий целевой функции
    r = matrix[inum][jnum] # коэф на пересечении выходящего и входящего векторов
    matrix[inum] /= r #делит строчку выходящего на нужный коэф.
    for i in [x for x in range(row) if x != inum]: #если x не выходящая строчка
        r = matrix[i][jnum]
        matrix[i] -= r * matrix[inum] #отнимает от строчки выходящую строчку умноженную на коэф.
def doNoMinus(matrix, row, col):
    f = True
    while f:
        a0 = []
        for i in range(0, row):
            a0.append(matrix[i][-1])
        if min(list(a0)) < 0:
            noMinus(a0, matrix, row, col)
        else:
            f = False
def noMinus(a0, matrix, row, col):

    jnum = a0.index(min(a0))

    m = []  # массив для поиска минимального значения
    for i in range(0, col - 1):
        if matrix[jnum][i] == 0 or matrix[jnum][i] == 1:
            m.append(0)
        else:
            m.append(matrix[jnum][i])

    inum = m.index(min([x for x in m if x < 0]))

    forChange = [] # вводит элементы для изменения матрицы
    for i in range(0, row):
        forChange.append(matrix[i][inum])

    basisVectors[jnum - 1] = inum  # [inum - 1] для того чтобы убрать первый в массиве член, принадлежащий целевой функции
    r = m[inum]  # коэф на пересечении выходящего и входящего векторов
    matrix[jnum] /= r  # делит строчку выходящего на нужный коэф.
    for i in [x for x in range(row) if x != jnum]:  # если x не выходящая строчка
        r = forChange[i]
        matrix[i] -= r * matrix[jnum]  # отнимает от строчки выходящую строчку умноженную на коэф.
def optimize(matrix, row, col):
    counter = 0
    flag = True
    while flag:
        cj = list(matrix[0][:9])  # Список значений целевой функции
        sum = 0
        sumArr = []  # массив сумм значений в матрице
        for i in range(0, col - 1):
            for j in range(1, row):
                sum += matrix[j][i]
            sumArr.append(sum)
            sum = 0
        jcj = []  # массив значений целевых функций базисных векторов
        for i in range(len(sumArr)):
            if sumArr[i] == 1.0:
                jcj.append(cj[i])

        deltaJ = []  # массив дельта жи
        deltaSum = 0
        test = []
        for i in range(0, col):
            for j in range(len(jcj)):
                deltaSum += (matrix[j][i] * jcj[j])
                test.append(deltaSum)
            deltaSum -= cj[i]
            deltaJ.append(deltaSum)
            deltaSum = 0
        if min(list(deltaJ[:-1])) >= 0: #Если нет отрицательных прекращаем
            counter += 1
            print("Итерация", counter)
            end = list(map(lambda x: x + 1, basisVectors))
            print("Базисные вектора = {", end, "}")
            print("Ваша текущая матрица")
            print('\n'.join([''.join(['{:25}'.format(x) for x in row])
                             for row in matrix]))
            print()
            flag = False
        else:
            counter += 1
            end = list(map(lambda x: x + 1, basisVectors))
            print("Итерация", counter)
            print("Базисные вектора = {", end, "}")
            VectorChange(matrix, row, col)#Иначе следующая итерация

def optimizeOutputMax(matrix, col):
    for i in range(col - 1):
        if i in basisVectors:
            print("x"+str(i + 1)+"=%.2f" % matrix[basisVectors.index(i)+1][-1])
        else:
            print("x"+str(i + 1)+"=0.00")
    print("оптимальное максимизированное значение = %.2f"%(-matrix[0][-1]))
def optimizeOutputMin(matrix, col):
    for i in range(col - 1):
        if i in basisVectors:
            print("x"+str(i + 1)+"=%.2f" % matrix[basisVectors.index(i)+1][-1])
        else:
            print("x"+str(i + 1)+"=0.00")
    print("оптимальное минимизированное решение значение = %.2f"%(-matrix[0][-1]))

print("Лабораторная работа по ИО №2")
while(True): #Вывод информации на экран
    print("\n1 - симплекс решение прямой задачи\n")
    print("2 - симплекс решение двойственной задачи\n")
    print("3 - выход\n")
    print("----------------------------------------------------------------------------------------")
    choice = int(input())
    if choice == 1:
        matrix = np.loadtxt("data.txt", dtype=float)
        (row, col) = matrix.shape
        basisVectors = list(range((col - 1) - (row - 1), col - 1))
        doNoMinus(matrix, row, col)
        optimize(matrix, row, col)
        optimizeOutputMax(matrix, col)
    if choice == 2:
        matrix = np.loadtxt("datanew.txt", dtype=float) #Загрузка матрицы в программу из файла
        (row, col) = matrix.shape #Возвращает размерность массива
        basisVectors = list(range((col - 1) - (row - 1), col - 1)) #первые базисные вектора
        doNoMinus(matrix, row, col) #Вызов функции убирающие отрицательные значения ограничений
        optimize(matrix, row, col) #поиск оптимального решения
        optimizeOutputMin(matrix, col) #печать ответа
    if choice == 3:
        break
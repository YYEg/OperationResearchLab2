import numpy as np
def pivot(matrix, bn):
    l = list(matrix[0][:-1]) #Знач.цел.функ.
    jnum = l.index(max(l)) # Номер перевода

    m = []
    for i in range(bn):
        if matrix[i][jnum] == 0:
            m.append(0)
        else:
            m.append(matrix[i][-1] / matrix[i][jnum])
    inum = m.index(min([x for x in m[1:] if x!=0]))  # Перенести нижний индекс
    s[inum-1] = jnum
    r = matrix[inum][jnum]
    matrix[inum] /= r
    for i in [x for x in range(bn) if x !=inum]:
        r = matrix[i][jnum]
        matrix[i] -= r * matrix[inum]
def solve(d,bn):
    flag = True
    while flag:
        if max(list(d[0][:-1])) <= 0: # Пока все коэффициенты не будут меньше или равны 0
            flag = False
        else:
            pivot(d,bn)
def printSol(d,cn):
    for i in range(cn - 1):
        if i in s:
            print("x"+str(i)+"=%.2f" % d[s.index(i)+1][-1])
        else:
            print("x"+str(i)+"=0.00")
    print("objective is %.2f"%(-d[0][-1])) #%.2f - ограничивает числа после запятой, f - float, % для подстановки
d = np.loadtxt("./data.txt", dtype=np.float)
(bn,cn) = d.shape
s = list(range(cn-bn,cn-1)) # Базовый список переменных
solve(d,bn)
printSol(d,cn)
import numpy as np
import timeit
from numpy import linalg as LA
print("Возведение матрицы А размерностью 3х3 в степень -1")
A = []
for i in range(3):
    A.append([])
    for j in range(3):
        print("Введите элемент матрицы с индексом ", i + 1, j + 1, ":", end='')
        k = int(input())
        A[i].append(k)
start_time = timeit.default_timer()
a = np.array(A)
print("Матрица А: ", a, sep='\n')
o = np.linalg.det(a)
if o == 0:
    print("Матрица А в стемени -1 не существует, так как определитель матрицы А равен 0.")
else:
    b = np.linalg.inv(a)
    print("Матрица А в степени -1: ", b, sep='\n')
print("Время работы программы: ",timeit.default_timer() - start_time)

import numpy as np
b=int(input("Введите одно из предложенных действий: \n1)Транспонирование матрицы (возможные размеры матриц: 1х2, 2х1, 1х3, 3х1,2х2, 3х3) \n2)Умножение матриц (возможные размеры матриц: 1х2, 2х1, 1х3, 3х1, 2х2, 3х3)\n3)Определение ранга матрицы (возможные размеры матриц: 2х2, 3х3))\n"))
if b==1:
    print("Введите размерность матрицы")
    n, m = int(input("Строки:")), int(input("Столбцы:"))
    print(n, "x", m)
    A = []
    for i in range(n):
        A.append([])
        for j in range(m):
            print("Введите элемент матрицы с индексом ", i + 1, j + 1, ":", end='')
            k = int(input())
            A[i].append(k)
    a = np.array(A)
    print("Матрица А: ", a, sep='\n')
    print("Транспонированая матрица А:", a.transpose(), sep='\n')
elif b==2:
    print("Введите размерность матрицы A")
    n, m = int(input("Строки:")), int(input("Столбцы:"))
    print(n, "x", m)
    a = []
    for i in range(n):
        a.append([])
        for j in range(m):
            print("Введите элемент матрицы A с индексом ", i + 1, j + 1, ":", end='')
            k = int(input())
            a[i].append(k)
    A = np.array(a)
    print("Введите размерность матрицы B:", sep='\n')
    c, d = int(input("Строки:")), int(input("Столбцы:"))
    if m == c:
        print(c, "x", d)
        b = []
        for i in range(c):
            b.append([])
            for j in range(d):
                print("Введите элемент матрицы B с индексом ", i + 1, j + 1, ":", end='')
                k = int(input())
                b[i].append(k)
        B = np.array(b)
    else:
        print("Умножение матрицы А на В невозиожно.")
    print("Матрица А: ", A, sep='\n')
    print("Матрица B: ", B, sep='\n')
    C = A.dot(B)
    print("Результат умножение матрицы А на матрицу В:", C, sep='\n')
elif b==3:
    print("Введите размерность матрицы")
    n, m = int(input("Строки:")), int(input("Столбцы:"))
    print(n, "x", m)
    a = []
    for i in range(n):
        a.append([])
        for j in range(m):
            print("Введите элемент матрицы с индексом ", i + 1, j + 1, ":", end='')
            k = int(input())
            a[i].append(k)
    A = np.array(a)
    r = np.linalg.matrix_rank(A)
    print("Матрица А: ", A, sep='\n')
    print("Ранг матрицы А равен: ", r)

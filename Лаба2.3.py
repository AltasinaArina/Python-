import copy
import timeit
start_time = timeit.default_timer()
a = []
for i in range(3):
    a.append([])
    for j in range(3):
        print("Введите элемент матрицы с индексом ", i + 1, j + 1, ":", end='')
        k=int(input())
        a[i].append(k)
for i in range(3):
    print()
    for j in range(3):
        print(a[i][j],end=' ')
h=(a[0][0]*a[1][1]*a[2][2] + (a[0][1]*a[1][2]*a[2][0]) + (a[1][0]*a[2][1]*a[0][2])) - a[0][2]*a[1][1]*a[2][0] - a[0][1]*a[1][0]*a[2][2] - a[1][2]*a[2][1]*a[0][0]
l=[]
print()
for i in range(3):
    l.append([])
    for j in range(3):
        l[i].append(0)

def f(a,i,j):
    p = copy.deepcopy(a)
    del p[i]
    for o in range(2):
        del p[o][j]
    g=(((-1)**(i+2+j)))*(p[0][0]*p[1][1]-(p[0][1]*p[1][0]))
    return g
for i in range(3):
    for j in range(3):
        l[i][j] = f(a, i, j)*(1/h)
t=[]
for i in range(3):
    t.append([])
    for j in range(3):
        t[i].append(l[j][i])
for i in range(3):
    print()
    for j in range(3):
        print(t[i][j],end=" ")
print(sep='\n')
print("Время работы программы: ",timeit.default_timer() - start_time)
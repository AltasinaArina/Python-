print("Введите количество элементов списка: ")
n = int(input())
print("Введите элементы списка: ")
a = [int(input()) for i in range(n)]
print(a)
for j in range(n-1):
    for i in range(n-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1],a[i]
print(a)
print("Сложность данного алгоритма: О(n^2)")
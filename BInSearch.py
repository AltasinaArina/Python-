n = int(input("Введите количество элементов в списке: "))
a = []
for i in range(n):
    print("Введите элемент списка с индексом ", i + 1, ":", end='')
    p = int(input())
    a.append(p)
a.sort()
print(a)
t = int(input("Введите элемент поиска: "))
n = 0
x = len(a) // 2
l = 0
h = len(a) - 1
while a[x] != t and l <= h:
    if t > a[x]:
        l = x + 1
    else:
        h = x - 1
    x = (l+h) // 2
    n += 1
if l > h:
    print("Данный элемент отсутсвует в списке")
else:
    print("Данный элемент есть в списке")
    print("Количество интераций: ", n)
print("Введите скобки")
a = list(input())
if len(a) == 0:
    print("Скобки отсутствуют!")
elif len(a) == 1:
    print("Скобка, нарушающая порядок под индексом [0]")
else:
    k = 0
    n = len(a)
    for i in range(1,n,2):
        for j in range(n):
            if i+j < n:
                if (a[j] == "(") and (a[i+j] == ")"):
                    a[j] = 0
                    a[i+j] = 0
    for i in range(n):
        if a[i] != 0:
            print("Скобка, нарушающая порядок под индексом [", i, "]")
            break
        else:
            k += 1
if k == n:
    print("Все скобки расставлены правильно!")
import math
print("Введите функцию из перечня: сложение, вычитание, деление, умножение, возведение в степень, логарифм, округление в большую сторону, округление в меньшую сторону")
fun = input()
if fun == "возведение в степень":
    print("Введите число, которое будет возводиться в степень")
    a = int(input())
    print("Введите степень, в которую нужно возвести число")
    b = int(input())
    c = a ** b
if fun == "логарифм":
    print("Введите число")
    a = int(input())
    print("Введите основание логарифма")
    b = int(input())
    c = math.log(a,b)
if fun == "сложение":
    print("Введите первое число")
    a = int(input())
    print("Введите второе число")
    b = int(input())
    c = a + b
if fun == "вычитание":
    print("Введите первое число")
    a = int(input())
    print("Введите второе число")
    b = int(input())
    c = a - b
if fun == "деление":
    print("Введите первое число")
    a = int(input())
    print("Введите второе число")
    b = int(input())
    c = a / b
if fun == "умножение":
    print("Введите первое число")
    a = int(input())
    print("Введите второе число")
    b = int(input())
    c = a * b
if fun == "округление в большую сторону":
    print("Введите число")
    a = float(input())
    print("Введите до какого числа после запятой округлять")
    b = int(input())
    c = round(a, b)
    m = [5, 6, 7, 8, 9]
    l = [1, 2, 3, 4, 5]
    n = str(a)
    k = int(n[-1])
    x = 1 / (10 ** b)
    if a > 0:
        if k in l:
            c = c + x
    else:
        if k in m:
            c = c + x
if fun == "округление в меньшую сторону":
    print("Введите число")
    a = float(input())
    print("Введите до какого числа после запятой округлять")
    b = int(input())
    c = round(a, b)
    m = [5, 6, 7, 8, 9]
    l = [1, 2, 3, 4, 5]
    n = str(a)
    k = int(n[-1])
    x = 1 / (10 ** b)
    if a > 0:
        if k in m:
            c = c - x
    else:
        if k in l:
            c = c - x
print("Результат вычисления равен ",c)


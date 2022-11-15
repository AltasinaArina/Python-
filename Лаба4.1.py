import time
import fast
import comb
print('Введите количесво элементов в списке: ')
n = int(input())
a = [int(input()) for i in range(n)]
print("Изначальный список: ", a)
print("Выберете метод сортировки: Быстрая, Расчёска")
o = input()
if o == "Быстрая":
    start = time.perf_counter()
    fast.sort(a, 0, len(a))
    finish = time.perf_counter()
    print("Вычесление заняло: ", finish-start, " секунд")
    print("Отсортированный список:", a)
else:
    start = time.perf_counter()
    comb.comb(a)
    finish = time.perf_counter()
    print("Вычесление заняло: ", finish - start, " секунд")
    print("Отсортированный список:", a)

print("Введите Ваше имя")
name = input()
print("Введите Ваш возраст")
age = int(input())
child = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
young = [18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44]
old = [45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
a = (11,12,13,14)
print("Меня зовут",name)
c = age % 10
if c == 1 and age != 11:
    print("Мне ",age,"год.")
elif (c == 2 or c == 3 or c == 4) and (age != 12 or age != 13 or age != 14):
    print("Мне ",age,"года.")
elif age in a:
    print("Мне ",age,"лет.")
else:
    print("Мне ",age,"лет.")
if age in child:
    print("Вы ребёнок!")
elif age in young:
    print("Вы молодёжь!")
else:
    print("Вы в зрелом возрасте!")

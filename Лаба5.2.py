import numpy
import random
import matplotlib.pyplot
print('Введите количесвто элементов в списке:')
n = int(input())
a = []
for i in range(n):
    a.append(random.randint(0,100))
print(a)
mean = sum(a)/n
print ("Математическое ожидание:", mean)
s = (sum((i-mean)**2 for i in a)/n) ** 0.5
print("Среднеквадратичное отклонение:", s)
k = random.randint(0,100)
b = random.randint(0,100)
f = numpy.array([k*i+b for i in range (n)])
y = f+numpy.random.normal(mean, s, n)
x = numpy.array(range (n))
mx = sum(x)/n
my = sum(y)/n
ax = numpy.dot(x.T, x)/n
ay = numpy.dot(x.T, y)/n
k1 =(ay-mx*my)/(ax-mx**2)
b1 = my-k1*mx
f1 = numpy.array([k1*i+b1 for i in range (n)])
matplotlib.pyplot.plot(f1,c='red')
matplotlib.pyplot.scatter(x, y)
matplotlib.pyplot.grid()
matplotlib.pyplot.show()

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from scipy.stats import norm

#M = 22695477
M = 101 #множитель
C = 1 #приращение
p = 2 ** 14 #модуль (простое число или ст 2)

flag = True

# Возвращает два значения:
# Первое значение, которое является нормализованным (от 0 до 1) псевдослучайным числом, вычисленным как ( U_{new} / p ).
# Второе значение, которое представляет собой новое значение ( U_{new} ), которое может быть использовано
# как текущее значение для следующего вызова функции.
def get_random(U, M, C, p):
    U_new = (U * M + C) % p
    return U_new / p, U_new


def get_random_array(length):
    U = [0]
    R = []
    global M, C, p
    for i in range(length - 1):
        rand, U_new = get_random(U[-1], M, C, p)
        R.append(rand)
        U.append(U_new)

    return R


def get_L():
    numbers = []
    U = [0]
    global M, C, p, flag
    R = []
    rand, num = get_random(U[-1], M, C, p)
    while num not in numbers:
        U.append(num)
        R.append(rand)
        numbers.append(num)
        rand, num = get_random(U[-1], M, C, p)
        if len(R) > 10000 and flag:
            print('Более 10000. Продолжить? Y/n')
            if input() != 'Y':
                return len(U)
            else:
                flag = False

    return len(R)


print('Наибольшая длина неповторяющихся элементов: ', get_L())


b = 0.99
d = 0.01
N = int((norm.ppf((1 - b) / 2) / (2 * d)) ** 2)

random_array = get_random_array(N)

sns_plot = sns.distplot(random_array)
fig = sns_plot.get_figure()
plt.show()

x = [random_array[2 * i] for i in range(len(random_array) // 2)]
y = [random_array[2 * i + 1] for i in range(len(random_array) // 2)]

hist, x_edges, y_edges = np.histogram2d(x, y, bins=10)

plt.imshow(hist, extent=[x_edges[0], x_edges[-1], y_edges[0], y_edges[-1]])
plt.xticks(ticks=x_edges)
plt.xlabel('x')
plt.yticks(ticks=y_edges)
plt.ylabel('y')
plt.show()

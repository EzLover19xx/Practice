import math

a = int(input())
b = int(input())
c = int(input())
ariph = (a + b + c) / 3
geom = (a * b * c) ** (1 / 3)
print(ariph, geom)


def func(x):
    return x ** 3 + x ** 2 - (3 / 4)


print("Введите значения x")
xmas = []
for i in range(3):
    x = int(input())
    xmas.append(x)
print("y1 =", func(xmas[0]), '\n', "y2 =", func(xmas[1]), '\n', "y3 =", func(xmas[2]), '\n')

print("Введите стороны треугольника")
A = int(input())
B = int(input())
C = int(input())
print("Периметр треугольника равен:", A + B + C)

print("Введите ребро куба")
A = int(input())
print("Объем куба равен", A ** 3, "Площадь его боковых поверхностей равна:", A ** 2)

print("Введите радиус шара:")
r = int(input())
V = (4 / 3) * math.pi * (r ** 3)
print("Объем шара равен =", V)

print("Введите сторону равностороннего треугольника:")
z = int(input())
s = ((3 ** 1 / 2) / 4) * a ** 2
print("Площадь равна: ", s)

print("Введите объем информации в байтах:")
b = int(input())
kb = b / 2 ** 10
mb = kb / 2 ** 10
gb = mb / 2 ** 10
print("Килобайт = ", kb, "Мегабайт = ", mb, "Гигабайт = ", gb)

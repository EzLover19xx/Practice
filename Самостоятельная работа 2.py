# print("Введите координаты x и y")
# x = int(input())
# y = int(input())
# chet = 0
# if x > 0 and y > 0:
#     chet = 1
# else:
#     if x > 0 and y < 0:
#         chet = 4
#     elif x < 0 and y < 0:
#         chet = 4
#     else:
#         chet = 2
# print(chet)
#
# x1 = int(input())
# x2 = int(input())
# print("Результат умножения первого числа на второе?")
# otv = int(input())
# if x1 * x2 == otv:
#     print("Ответ верный")
# else:
#     print("Вы ответили неправильно, правильный ответ:", otv)
#
# print("Введите три целых числа:")
# amas = []
# chisl = 0
# for i in range(2):
#     a = int(input())
#     amas.append(a)
# for i in range(2):
#     if amas[i] > 0 and amas[i] % 2 == 0:
#         chisl += 1
# print(chisl)

print("Введите точки A,B,C")
A = int(input())
B = int(input())
C = int(input())
if abs(B - A) > abs(C - A):
    print("Точка C ближе, ее растояние равно = ", abs(C - A))
else:
    print("Точка B ближе и ее расстояние равно = ", abs(B - A))

print("Последовательно введите координаты трех вершин в формате - сначала x первой вершины, затем y первой вершины")
xmas = []
ymas = []
for i in range(3):
    x = int(input())
    xmas.append(x)
    y = int(input())
    ymas.append(y)
if xmas.count(xmas[0]) > 1:
    print(xmas.index(xmas[0],1))
else xmas.count(xmas[1]) > 1:
    if xmas.index(xmas[1]) < 1:

if ymas.count(ymas[0]) > 1:
    print(ymas.index(ymas[0],1))
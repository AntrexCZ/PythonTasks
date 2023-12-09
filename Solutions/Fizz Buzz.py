"""
Сверх классическая задача fizz buzz на вход идет 3 числа. последнее больше двух предыдущих

Надо распечатать числа от 1 до третьего, причем если число делиться на первое, то вместо него печатаем букву F,
если делиться на второе то букву B, если делиться на оба то FB

Примеры

на входе
3 5 17
выход
1 2 F 4 B F 7 8 F B 11 F 13 14 FB 16 17

вход
2 3 10
выход
1 F B F 5 FB 7 F B F

Вход
3 4 6
Выход
1 2 F B 5 F

"""

empty = []
x = input("Enter 3 numbers, separated by coma : ").split(",")
y = [int(i) for i in x]
y.sort()
print(y)
sorted_list = list(range(1, y[2] + 1))
y.pop()
print(sorted_list)
print(y)
for i in sorted_list:
    if i % y[0] == 0 and i % y[1] == 0:
        empty.append("FB")
    elif i % y[0] == 0:
        empty.append("X")
    elif i % y[1] == 0:
        empty.append("B")
    else:
        empty.append(str(i))

print(empty)
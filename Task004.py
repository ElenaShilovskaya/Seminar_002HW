# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции вводит пользователь через пробел.
# Не совсем поняла какой способ ввода позиций следует применять,
# ввод вручную реализован, исходя из информации в чате тг

n = 5
elements = list(range (-n, n+1))
print(elements)
positions = (input(f'Введите через пробел любые номера позиций от 1 до {n*2 + 1}: ').split(' '))
positions = list(map(int, positions))
print(positions)
mult = 1
for i in range(len(positions)):
    mult *= elements[positions[i]-1]
print(mult)

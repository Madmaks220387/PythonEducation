# Задание 4
# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

numb = abs(int(input("Введите целое положительное число: ")))
max = numb % 10
while numb >= 1:
    numb = numb // 10
    if numb % 10 > max:
        max = numb % 10
    if numb > 9:
        continue
    else:
        print(f"Максимальное цифра - {max}")
        break
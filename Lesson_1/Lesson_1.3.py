# Задание 3
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

numb = int(input("Введите число: "))
total = (numb + int(str(numb) + str(numb)) + int(str(numb) + str(numb)+ str(numb)))
print(f"Сумма чисел n + nn + nnn = {total}")
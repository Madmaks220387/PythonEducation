# Реализовать функцию, принимающую два числа
# (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.


def my_func(*args):

    try:
        arg1 = int(input("Введите делимое: "))
        arg2 = int(input("Введите делитель: "))
        result = arg1 / arg2
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    except ValueError:
        return 'Value error'

    return result


print(f"Результат деления = {my_func()}")
# Реализовать функцию, принимающую несколько параметров, описывающих
# данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных
# о пользователе одной строкой.


def my_func(name, surname, birthday, city, email, phone):
    print(name, surname, birthday, city, email, phone)

my_func(name= 'Max', surname='Sheldov', birthday=1987, city='Kaliningrad', email='email@mail.ru', phone='89068877463')
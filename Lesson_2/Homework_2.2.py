# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

elem_count = int(input("Какое количество элементов списка вы хотите: "))
my_list = []
ind = 0
elem = 0
while ind < elem_count:
    my_list.append(input("Введите элемент списка: "))
    ind += 1

if len(my_list) % 2 == 0:
    ind = 0
    while ind < len(my_list):
        my_list[ind], my_list[ind+1] = my_list[ind+1], my_list[ind]
        ind += 2
else:
    ind = 0
    while ind < len(my_list) - 1:
        my_list[ind], my_list[ind+1] = my_list[ind+1], my_list[ind]
        ind += 2
print("\n"f"Обмен значениями произошел - {my_list}")
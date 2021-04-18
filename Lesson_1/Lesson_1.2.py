# Задание 2

total = int(input("Введите время в секундах: "))
hours = total // 3600
minutes = (total - hours * 3600) // 60
seconds = total - (hours * 3600 + minutes *60)
print("Преобразование времени в формат чч:мм:сс - %02d:%02d:%02d" % (hours, minutes, seconds))

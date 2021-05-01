# Реализовать функцию int_func(), принимающую слово из маленьких
# латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать
# строка из слов, разделенных пробелом. Каждое слово состоит
# из латинских букв в нижнем регистре. Сделать вывод исходной
# строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def int_func(a):
    sep_word = a.split(' ')
    res = []
    for i in sep_word:
        str_el = str(i)
        f_letter = str_el[:1].upper()
        word = f_letter + str_el[1:]
        res.append(word)
    return res


print(*int_func("hello python hello world"))
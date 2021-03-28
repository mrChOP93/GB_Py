# Пилить разные доп проверки на формат вводимых данных и вывод соответствующих ошибок с предложением повторного воода-
# мне было лень
import json
from functools import reduce
from itertools import count, cycle


def choose_lesson():
    nom_task = None
    while nom_task != 's':
        nom_task = input('Введите номер занятия, для прекращения работы, введите s: ')
        if nom_task == '1':
            lesson1()
        elif nom_task == '2':
            lesson2()
        elif nom_task == '3':
            lesson3()
        elif nom_task == '4':
            lesson4()
        elif nom_task == '5':
            lesson5()


def lesson1():
    nom_task = None
    while nom_task != 'l':
        nom_task = input('Введите номер задания, для перехода к выбору занятия, введите l: ')
        if nom_task == '1':
            print('Задание 1')
            my_var1 = input('Введите значение переменной 1: ')
            my_var2 = input('Введите значение переменной 2: ')
            my_var3 = input('Введите значение переменной 3: ')
            print(my_var1, my_var2, my_var3, sep=';\n')
        elif nom_task == '2':
            time = int(input('Введите время в секундах: '))
            print(f'Форматированное время: {int(time / 3600)}:{int(time / 60 % 60)}:{int(time % 60)}')
        elif nom_task == '3':
            nom = input('Введите суммируемое число: ')
            nom2 = int(nom + nom)
            nom3 = int(nom + nom + nom)
            nom = int(nom)
            print((nom + nom2 + nom3))
        elif nom_task == '4':
            nom = int(input('Введите целое положительное число число:'))
            n = 1
            del_ost = 10
            max_nom = 0
            while n <= len(str(nom)):
                cur_nom = nom % del_ost
                if cur_nom > max_nom:
                    max_nom = cur_nom
                n += 1
                del_ost = del_ost * 10
            print(max_nom)
        elif nom_task == '5':
            prof = int(input('Введите прибыль: '))
            cost = int(input('Введите издержку фирмы: '))
            prof_dif = prof - cost

            if prof_dif > 0:
                print('Фирма отработала с прибылью ', prof_dif)
                print('Рентабельность: ', (prof / cost))
                worker = int(input('Введите количество сотрудников: '))
                print('Прибыль на сотрудника: ', (prof_dif / worker))
            else:
                print('Фирма отработала с убытком: ', prof_dif)
        elif nom_task == '6':
            res = float(input('Введите начальное расстояние: '))
            target = float(input('Введите цель: '))
            day = 1
            while res < target:
                print(day, '-й день: ', format(res, '.2f'))
                day += 1
                res = res + res / 10
            print('Ответ: на ', day, '-й день спортсмен достиг результата — не менее ', target, ' км.')
    choose_lesson()


def lesson2():
    nom_task = None
    while nom_task != 'l':
        nom_task = input('Введите номер задания, для перехода к выбору занятия, введите l: ')
        if nom_task == '1':
            my_ls = list()
            data = input('Введите через пробел поочередно данные типа int, str, float.'
                         'Остальные данные будут представлены ввиде str: ')
            data = data.split()
            et = 1
            for el_data in data:
                if et == 1:
                    el_data = int(el_data)
                elif et == 2:
                    el_data = str(el_data)
                elif et == 3:
                    el_data = float(el_data)
                my_ls.append(el_data)
                et += 1
            print(my_ls)
            for el_my_ls in my_ls:
                print(f'Значение данных: {el_my_ls}, тип данных: {type(el_my_ls)}')
        elif nom_task == '2':
            data = input('Введите через пробел поочередно данные: ')
            data = data.split()
            print(data)
            len_data = len(data)
            even_data = len_data % 2 == 0
            if even_data:
                len_data += -1
            else:
                len_data += -2
            et = 0
            while et <= len_data:
                f_el = data[et]
                data[et] = data[et + 1]
                data[et + 1] = f_el
                et += 2
            print(data)
        elif nom_task == '3':
            month = int(input('Введите номер месяца: '))
            month_dict = {'winter': [1, 2, 12], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
            for key, value in month_dict.items():
                if month in value:
                    print(key)
        elif nom_task == '4':
            data = input('Введите последовательность слов через пробелы: ')
            data = data.split()
            et = 1
            for wrd in data:
                print(f'{et} {wrd[:10]}')
                et += 1
        elif nom_task == '5':
            data = int(input('Введите натуральное число: '))
            my_ls = [7, 5, 3, 3, 2]
            print(f'Исходный: {my_ls}')
            my_ls.append(data)
            my_ls.sort(reverse=True)
            print(f'Конечный: {my_ls}')
        elif nom_task == '6':
            prod_lst = list()
            et = 1
            data = None
            while data != 'n':
                name = input('Введите название: ')
                price = input('Введите количество: ')
                nom = input('Введите цену: ')
                unit = input('Введите ед.измерения: ')
                prod_lst.append((et, {'Название': name, 'Цена': price, 'Количество': nom, 'ед.': unit}))
                et += 1
                data = input('Продолжить ввод товаров y/n? ')
            for el in prod_lst:
                print(el)


def lesson3():
    nom_task = None
    while nom_task != 'l':
        nom_task = input('Введите номер задания, для перехода к выбору занятия, введите l: ')
        if nom_task == '1':
            def division(num1, num2):
                if num2 == 0:
                    return 'Нельзя делить на ноль!'
                else:
                    return num1 / num2

            print(division(float(input('Введите делимое: ')), float(input('Введите делитель: '))))
        elif nom_task == '2':
            def full_name(name, surname, patronymic, birth):
                return [name, surname, patronymic, birth]

            print(full_name(birth=input('Введите др: '), surname=input('Введите фамилию: '),
                            name=input('Введите имя: '), patronymic=input('Введите отчество: ')))
        elif nom_task == '3':
            def my_func(num1, num2, num3):
                nums = [num1, num2, num3]
                i = 1
                num_sum = 0
                while i != 3:
                    max_num = max(nums)
                    num_sum += max_num
                    nums.remove(max_num)
                    i += 1
                return num_sum

            print(my_func(float(input('Введите первое число: ')), float(input('Введите второе число: ')),
                          float(input('Введите третье число: '))))
        elif nom_task == '4':
            def degree(num1, num2):
                return num1 ** num2

            def ass_degree(num1, num2):
                i = -1
                deg_num = num1
                while i > num2:
                    deg_num = deg_num * num1
                    i += -1
                return 1 / deg_num

            var_calc = input('Если хотите провести расчет нормальным методом, введите 1,'
                             'если хотите методом "через жопу к звездам", введите 2,'
                             'если хотите получить результат обоих методов, введите 3: ')
            num1 = int(input('Введите первое число: '))
            num2 = int(input('Введите второе число: '))
            if var_calc == '1':
                print(degree(num1, num2))
            elif var_calc == '2':
                print(ass_degree(num1, num2))
            elif var_calc == '3':
                print(f'Норм:    {degree(num1, num2)}')
                print(f'Не норм: {ass_degree(num1, num2)}')
        elif nom_task == '5':
            sum_num = 0
            num = None
            while num != '!':
                data = input('Введите числа через пробел, для завершения введите "!": ').split()
                for num in data:
                    if num == '!':
                        break
                    sum_num += float(num)
                print(sum_num)
        elif nom_task == '6' or nom_task == '7':
            def str_title(st):
                return st.title()

            def multi_title(st):
                end_st = ''
                smm = st.split()
                i = 0
                for sm in smm:
                    smm[i] = str_title(smm[i])
                    i += 1

                return " ".join(smm)

            print(multi_title(input('Введите слова: ')))


def lesson4():
    nom_task = None
    while nom_task != 'l':
        nom_task = input('Введите номер задания, для перехода к выбору занятия, введите l: ')
        if nom_task == '1':
            print('см. l4_t1_param.py')
        elif nom_task == '2':
            lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
            print([j for i, j in zip(lst, lst[1:]) if j > i])
        elif nom_task == '3':
            print([el for el in range(20, 240) if (el % 20 == 0 or el % 21 == 0)])
        elif nom_task == '4':
            lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
            print([el for el in lst if lst.count(el) < 2])
        elif nom_task == '5':
            def sum_all(a, b):
                return a + b

            print(reduce(sum_all, [el for el in range(100, 1000) if el % 2 == 0]))
        elif nom_task == '6':
            ver_iter = input('1. Генератор целых чисел\n2. Повторитель\nВведите номер желаемого итератора: ')
            if ver_iter == '1':
                start_iter = int(input('Введите стартовое число: '))
                end_iter = int(input('Введите конечное число: '))
                print([el for el in range(start_iter, end_iter + 1)])
                for el in count(start_iter, 1):
                    if el > end_iter:
                        break
                    else:
                        print(el)
            elif ver_iter == '2':
                lst = input('Введите список повторяемых элементов через пробел: ').split()
                i = int(input('Введите количество повторений: '))
                it = 1
                for el in cycle(lst):
                    if it > i * len(lst):
                        break
                    print(el)
                    it += 1
        elif nom_task == '7':
            last_nom = int(input('Введите последнее число для факториала: '))

            def generator():
                for el in range(1, last_nom + 1):
                    yield el

            nom = 1
            for el in generator():
                nom *= el
                print(f'{el}! = {nom}')


def lesson5():
    nom_task = None
    while nom_task != 'l':
        nom_task = input('Введите номер задания, для перехода к выбору занятия, введите l: ')
        if nom_task == '1':
            with open('1t.txt', 'w', encoding='utf-8') as wf:
                lst = list()
                while True:
                    w_str = input('Введите записываемые данные: ')
                    if w_str != '':
                        if len(lst) > 0:
                            lst.append('\n' + w_str)
                        else:
                            lst.append(w_str)
                    else:
                        break
                wf.writelines(lst)
        elif nom_task == '2':
            with open('2t.txt', 'r', encoding='utf-8') as rf:
                print(f'Исходный текст:\n{rf.read()}')
                rf.seek(0)
                lns = rf.readlines()
                print(f'Всего строк: {len(lns)}')
                i = 1
                for el in lns:
                    print(f'В строке {i} слов {len(el.split())} ')
                    i += 1
        elif nom_task == '3':
            with open('3t.txt', 'r', encoding='utf-8') as rf:
                print(f'Исходный текст:\n{rf.read()}')
                rf.seek(0)
                lns = rf.readlines()
                i = 0
                salary = 0
                for el in lns:
                    split_str = el.split()
                    split_salary = float(split_str[1])
                    salary += float(split_salary)
                    if split_salary < 20000:
                        print(f'Работник с зп < 20к: {" ".join(split_str)}')
                    i += 1
                print(f'Средняя зп: {salary / i}')
        elif nom_task == '4':
            with open('4t.txt', 'r', encoding='utf-8') as rf:
                print(f'Исходный текст:\n{rf.read()}')
                rf.seek(0)
                nom_dict = {'One': 'Адын', 'Two': 'Дыва', 'Three': 'Тыри', 'Four': 'Четыре'}
                with open('4_1t.txt', 'w+', encoding='utf-8') as wf:
                    lns_f = rf.readlines()
                    lst = list()
                    for el in lns_f:
                        split_str = el.split(' — ')
                        lst.append(' — '.join([nom_dict.get(split_str[0]), split_str[1]]))
                    wf.writelines(lst)
                    wf.seek(0)
                    print(f'Получившийся текст:\n{wf.read()}')
        elif nom_task == '5':
            with open('5t.txt', 'w', encoding='utf-8') as wf:
                noms = '4 654 6 65 51 58 32 89 5 984 54'
                wf.write(noms)
                print(sum([int(el) for el in noms.split()]))
        elif nom_task == '6':
            with open('6t.txt', 'r', encoding='utf-8') as rf:
                print(f'Исходный текст:\n{rf.read()}')
                rf.seek(0)
                lns_f = rf.readlines()
                less_dic = dict()
                for ln in lns_f:
                    split_str = ln.split()
                    name_less = str(split_str[0])[:len(split_str[0]) - 1]
                    less = 0
                    i = 1
                    while i < len(split_str):
                        nom_s = split_str[i].find('(')
                        if nom_s != -1:
                            less += int(split_str[i][:nom_s])
                        i += 1
                    less_dic.update({name_less: less})
                print(less_dic)
        elif nom_task == '7':
            with open('7t.txt', 'r', encoding='utf-8') as rf:
                print(f'Исходный текст:\n{rf.read()}')
                rf.seek(0)
                lns_f = rf.readlines()
                lst = list()
                dct = dict()
                for ln in lns_f:
                    split_str = ln.split()
                    dct[split_str[0]] = (int(split_str[2]) - int(split_str[3]))
                lst.append(dct)
                average_profit = 0
                i = 0
                for el in dct.values():
                    if el >= 0:
                        average_profit += el
                        i += 1
                if i > 0:
                    lst.append({'average_profit': average_profit / i})
                with open("7t.json", "w+") as write_f:
                    json.dump(lst, write_f)
                    write_f.seek(0)
                    print(f'Итоговый текст:\n{write_f.read()}')


if __name__ == '__main__':
    choose_lesson()

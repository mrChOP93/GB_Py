# Пилить разные доп проверки на формат вводимых данных и вывод соответствующих ошибок с предложением повторного воода-
# мне было лень

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


choose_lesson()

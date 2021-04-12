import datetime


class Date:
    def __init__(self, dmy):
        self.dmy = dmy

    @classmethod
    def dmy_to_int(cls, dmy):
        splt = dmy.split('-')
        rtrn_splt = list()
        for i in splt:
            rtrn_splt.append(int(i))
        return rtrn_splt

    @staticmethod
    def valid(dmy):
        try:
            datetime.datetime.strptime(dmy, '%d-%m-%Y')
            return 'Валидация прошла успешно'
        except ValueError:
            raise ValueError("Валидация даты не прошла")


class DelErr(Exception):
    def __init__(self, txt):
        self.txt = txt


class FloatErr(Exception):
    def __init__(self, txt):
        self.txt = f'{txt} не является числом!'

    @staticmethod
    def valid(el):
        try:
            float(el)
            return True
        except ValueError:
            return False


def ls8_2():
    try:
        i = int(input('Введите делимое: '))
        j = int(input('Введите делитель: '))
        if j == 0:
            raise DelErr('делитель равен 0!')
    except ValueError:
        print('Введите число!')
    except DelErr as err:
        print(err)
    else:
        print(i / j)


def ls8_1():
    dt = Date('50-01-2021')

    print(dt.dmy_to_int(dt.dmy))
    print(dt.valid(dt.dmy))


def ls8_3():
    el = ''
    lst = list()
    while el != 'stp':
        el = input('Введите число: ')
        if el != 'stp':
            try:
                fe = FloatErr(f'{el} не является числом!')
                if not fe.valid(el):
                    raise fe
            except FloatErr as err:
                print(err)
            else:
                lst.append(el)
    print(lst)


if __name__ == '__main__':
    # ls8_1()
    # ls8_2()
    ls8_3()

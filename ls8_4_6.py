# Можно было и лучше, на пример, указать вместимость склада и его проверять, но я хочу спать X_X
class Err(Exception):
    def __init__(self, txt):
        self.txt = txt


class Storage:
    availability = dict()

    def __str__(self):
        st = ''
        for key in self.availability:
            st += f'{key.name} {self.availability[key]} шт. \n'
        return st

    def in_storage(self, oal, quantity):
        try:
            quantity = int(quantity)
            if oal.__class__.__bases__[0] != OfficeAppliances:
                Err('Не верно указана орг техника')
        except ValueError:
            print('Не верно указано количество')
        except Err as er:
            print(er)
        else:
            oal_in = self.availability.get(oal)
            if oal_in is not None:
                quantity += oal_in
            self.availability.update({oal: quantity})

    def out_storage(self, oal, quantity, department):
        try:
            quantity = int(quantity)
            if oal.__class__.__bases__[0] != OfficeAppliances:
                Err('Не верно указана орг техника')
        except ValueError:
            print('Не верно указано количество')
        except Err as er:
            print(er)
        else:
            oal_in = self.availability.get(oal)
            if oal_in is not None:
                oal_in -= quantity
                if oal_in < 0:
                    print('Не удалось списать, на складе не хватает вабранной техники')
                else:
                    self.availability.update({oal: oal_in})
                    print(f'Списано {quantity} шт. {oal.name} в {department}')


class OfficeAppliances:

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


class Printer(OfficeAppliances):
    def __init__(self, name, cost, ps):
        OfficeAppliances.__init__(self, name, cost)
        self.print_speed = ps


class Scanner(OfficeAppliances):
    def __init__(self, name, cost, ss):
        OfficeAppliances.__init__(self, name, cost)
        self.scan_speed = ss


class CopyMachine(OfficeAppliances):
    def __init__(self, name, cost, cs):
        OfficeAppliances.__init__(self, name, cost)
        self.copy_speed = cs


def ls8_4_6():
    strg = Storage()

    prntr = Printer('Принтер', 125, '25 л/м')
    scnr = Scanner('Сканет', 125, '25 л/м')
    cm = CopyMachine('Копир', 125, '25 л/м')

    strg.in_storage(prntr, 20)
    strg.in_storage(prntr, 10)
    strg.in_storage(scnr, 10)
    strg.in_storage(cm, '2g0')
    print(strg)

    strg.out_storage(prntr, 20, 'Бух')
    print(strg)

    strg.out_storage(scnr, 'df', 'Столовая')
    print(strg)


if __name__ == '__main__':
    ls8_4_6()

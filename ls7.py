from abc import ABC, abstractmethod


class Matrix:
    def __init__(self, mtr):
        self.matrix_mtr = mtr

    def __str__(self):
        str_mtrix = ''
        for i in self.matrix_mtr:
            for ii in i:
                str_mtrix += str(ii) + " "
            str_mtrix += '\n'
        return str_mtrix

    def __add__(self, other):
        for i in range(len(self.matrix_mtr)):
            for j in range(len(self.matrix_mtr[0])):
                self.matrix_mtr[i][j] += other[i][j]
        return Matrix(self.matrix_mtr)


def ls7_1():
    matrix = Matrix([[1, 2, 3], [3, 2, 1], [5, 4, 3]])
    print(matrix)
    matrix += [[1, 2, 3], [3, 2, 1], [5, 4, 3]]
    print(matrix)


##############################################################################

class Clothes:
    def __init__(self, name):
        self.Clothes_name = name

    @abstractmethod
    def calculation(self):
        pass


class Overcoat(Clothes):
    def __init__(self, name, size):
        Clothes.__init__(self, name)
        self.Overcoat_size = float(size)

    @property
    def calculation(self):
        return self.Overcoat_size / 0.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, height):
        Clothes.__init__(self, name)
        self.Suit_height = float(height)

    @property
    def calculation(self):
        return 2 * self.Suit_height + 0.3


def ls7_2():
    overcoat = Overcoat('Пальто', 10)
    print(f'{overcoat.Clothes_name} {overcoat.calculation}')

    suit = Suit('Костюм', 20)
    print(f'{suit.Clothes_name} {suit.calculation}')


############################################

class Cell:
    def __init__(self, sum_cage):
        self.Cell_sum_cage = int(sum_cage)

    def __add__(self, other):
        return Cell(self.Cell_sum_cage + other.Cell_sum_cage)

    def __sub__(self, other):
        sb = Cell(self.Cell_sum_cage - other.Cell_sum_cage)
        return sb if sb.Cell_sum_cage > 0 else 'Сумма ячеек меньше 0!'

    def __mul__(self, other):
        return Cell(self.Cell_sum_cage * other.Cell_sum_cage)

    def __truediv__(self, other):
        return Cell(self.Cell_sum_cage / other.Cell_sum_cage)

    def make_order(self, num):
        st = ''
        j = 1
        i = 0
        nm = self.Cell_sum_cage + int(self.Cell_sum_cage / num)
        while i < nm:
            if j <= num:
                symbol = '*'
            else:
                symbol = '\n'
                j = 0
            st += symbol
            j += 1
            i += 1
        return st


def ls7_3():
    cell = Cell(14)
    print(cell.make_order(3))
    cell2 = Cell(14)
    cell3 = cell + cell2
    print(cell3.Cell_sum_cage)
    cell2 = Cell(13)
    cell3 = cell - cell2
    print(cell3.Cell_sum_cage)
    cell2 = Cell(13)
    cell3 = cell * cell2
    print(cell3.Cell_sum_cage)
    cell2 = Cell(13)
    cell3 = cell / cell2
    print(cell3.Cell_sum_cage)


if __name__ == '__main__':
    # ls7_1()
    # ls7_2()
    ls7_3()

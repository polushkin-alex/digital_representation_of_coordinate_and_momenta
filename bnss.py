import numpy as np
import matplotlib.pyplot as plt

def all_combinations(array):
    '''
    создаёт из списка объектов всевозможные уникальные пары с точностью до перестановки
    '''
    combinations = list()
    for i in array:
        for j in array:
            if i != j:
                if (i,j) not in combinations and (j,i) not in combinations:
                    combinations.append((i,j))
    return(combinations)

class BinaryNonsymmetricDigit():
    '''
    Объект класса -- цифра номер s в двоичной несимметричной системе на решётке из 2^{(n_{+} + n_{-})} узлов
    2^{n_{+}} - 2^{-n_{-}} -- "максимальное" число на решётке
    2^{-n_{-}} -- шаг решётки
    '''

    def __init__(self, n_plus_, n_minus_, s_=0):
        if s_ >= n_plus_ or s_ < -n_minus_:
            print('неподходящий номер цифры')
        else:
            self.n_plus = n_plus_
            self.n_minus = n_minus_
            self.s = s_
            self.lattice = np.arange(2 ** (n_plus_ + n_minus_)) * 2 ** (-n_minus_)
            self.values = np.zeros(2 ** (n_plus_ + n_minus_))
            for ix, x in enumerate(self.lattice):
                if x - (x // (np.power(2., (s_ + 1)))) * np.power(2., (s_ + 1)) < np.power(2., s_):
                    self.values[ix] = 0
                else:
                    self.values[ix] = 1

    def plot_digit(self):
        '''
        Отрисовывает график цифры на соответствующей решётке
        '''
        plt.figure(figsize=(20, 10))
        plt.title(f'График цифры номер {self.s} при $n_+$ = {self.n_plus}, $n_-$ = {self.n_minus}')
        plt.xlabel('$x$', fontsize=15)
        plt.ylabel(f'$c({self.s},x)$', fontsize=15)
        plt.scatter(self.lattice, self.values)

class BinaryNonsymmetricSystem():
    '''
    Всевозможные двоичные несимметричные цифры для заданных n_{+} и n_{-}
    '''
    def __init__(self, n_plus_, n_minus_):
        self.n_plus = n_plus_
        self.n_minus = n_minus_
        self.digit_nums = np.arange(-n_minus_, n_plus_,1)
        self.digits = [BinaryNonsymmetricDigit(n_plus_, n_minus_, s) for s in self.digit_nums]

    def digit_composition(self, s1, s2):
        '''
        генерирует решётку и значения c(s1,x) * c(s2,x) на ней
        '''
        if s1 not in self.digit_nums or s2 not in self.digit_nums:
            print('недопустимые номера цифр')
        else:
            ix1, = np.where(self.digit_nums == s1)[0]
            ix2, = np.where(self.digit_nums == s2)[0]
            print(ix1, ix2)
            digit_1 = self.digits[ix1]
            digit_2 = self.digits[ix2]
            product_lattice = digit_1.lattice
            product_values = digit_1.values * digit_2.values
            return(product_lattice, product_values)

    def plot_digit_composition(self, s1, s2, plot_digits = False):
        '''
        рисует c(s1, x) * c(s2, x) (x)
        '''
        if s1 not in self.digit_nums or s2 not in self.digit_nums:
            print('недопустимые номера цифр')
        else:
            product_lattice, product_values = self.digit_composition(s1, s2)
            plt.figure(figsize = (20,10))
            plt.title(f'$c({s1}, x) \cdot c({s2},x)$ при $n_+$ = {self.n_plus}, $n_-$ = {self.n_minus}', fontsize = 15)
            plt.xlabel('$x$', fontsize = 15)
            plt.ylabel(f'$c({s1}, x) \cdot c({s2},x)$', fontsize = 15)
            plt.scatter(product_lattice, product_values)
            if plot_digits:
                ix1, = np.where(self.digit_nums == s1)[0]
                ix2, = np.where(self.digit_nums == s2)[0]
                digit_1 = self.digits[ix1]
                digit_2 = self.digits[ix2]

                plt.figure(figsize = (20,10))
                plt.xlabel('$x$', fontsize = 15)
                plt.ylabel(f'$c({s1}, x)$', fontsize = 15)
                plt.scatter(digit_1.lattice, digit_1.values)

                plt.figure(figsize = (20,10))
                plt.xlabel('$x$', fontsize = 15)
                plt.ylabel(f'$c({s2},x)$', fontsize = 15)
                plt.scatter(digit_2.lattice, digit_2.values)
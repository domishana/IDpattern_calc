# coding=utf-8
import scipy.special as scsp

alphabet = 26
number_character = 9
all_character = alphabet + number_character


def calc_pattern(number):
    number_place_pattern = scsp.comb(8, number, True)
    return number_place_pattern*(number_character**number)*(alphabet**(8-number))


if __name__ == '__main__':
    all_pattern = all_character**8
    print(all_pattern)
    for i in range(9):
        pattern = calc_pattern(i)
        print("{0:.2%}, {1}通り".format(pattern/all_pattern, pattern))

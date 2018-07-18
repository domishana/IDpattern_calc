# coding=utf-8
import scipy.special as scsp

alphabet = 26
number_character = 9
all_character = alphabet + number_character


def calc_pattern(number):
    number_place_pattern = scsp.comb(8, number, True)
    return number_place_pattern*(number_character**number)*(alphabet**(8-number))


def calc_probability(number, the_probability):
    return scsp.comb(150, number)*(the_probability**number)*((1-the_probability)**(150-number))


if __name__ == '__main__':
    all_pattern = all_character**8
    print(all_pattern)
    sum_probability = 0
    for i in range(6, 9):
        pattern = calc_pattern(i)
        print("数字が{0}個, {1:.2%}, {2}通り".format(i, pattern/all_pattern, pattern))
        sum_probability += pattern/all_pattern
    print("{0:.2%}".format(sum_probability))

    probability = 0
    for j in range(3):
        probability += calc_probability(j, sum_probability)
    print('{:.2%}'.format(1-probability))

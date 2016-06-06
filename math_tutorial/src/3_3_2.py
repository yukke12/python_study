# -*- coding: utf-8 -*-
from collections import Counter

# simplelist = [4, 2, 1, 3, 4]
# c = Counter(simplelist)
# print(c.most_common(1)[0][0])


def calculate_mode(numbers):
    c = Counter(numbers)
    mode = c.most_common(1)
    return mode[0][0]

def frequency_table(numbers):
    table = Counter(numbers)
    numbers_freq = table.most_common()
    numbers_freq.sort()
    print('Number\tFrequency')
    for number in numbers_freq:
        print('{0}\t{1}'.format(number[0],number[1]))

if __name__ == '__main__':
    scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    frequency_table(scores)
    # mode = calculate_mode(scores)
    # print('The mode of the list of numvers is: {0}'.format(mode))
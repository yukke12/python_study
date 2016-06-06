# -*- coding: utf-8 -*-

def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s/N
    return mean

def calculate_median(numbers):
    numbers.sort()
    N = len(numbers)
    median = 0
    if N % 2 == 0:
        m1 = N/2
        m2 = N/2 + 1
        m1 = int(m1) -1
        m2 = int(m2) -1
        median = (numbers[m1] + numbers[m2]) / 2
    else:
        median = numbers[N - 1]
    return median

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    mean = calculate_mean(donations)
    N = len(donations)
    median = calculate_median(donations)
    print ('Median donation over the last {0} days is {1}'.format(N, median))

# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import math

def frange(start, end, increment):
    """
    :param start: 初期値 :param end: 終了値 :param increment: 増分
    :return: 浮動小数点のリスト
    """

    numbers = []
    while start < end:
        numbers.append(start)
        start += increment
    return numbers


def draw_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('x-cordinate')
    plt.ylabel('y-cordinate')
    plt.title('Gravitational force and distance')

def drow_trajectory(u, theta):
    theta = math.radians(theta)
    g = 9.8
    t_fright = 2 * u * math.sin(theta) / g # 飛行時間
    intervals = frange(0, t_fright, 0.001)
    x = []
    y = []
    for t in intervals:
        x.append(u * math.cos(theta) * t)
        y.append(u * math.sin(theta) * t - 0.5 * g * t * t)
    draw_graph(x, y)


if __name__ == '__main__':
    # u = 5 # 初速
    # theta = 45 # 入射角
    u_list = [20, 40, 60]
    theta = 45
    for u in u_list:
        drow_trajectory(u, theta)
    plt.show()

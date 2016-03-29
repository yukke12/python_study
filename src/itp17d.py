# -*- coding: utf-8 -*-
# n×m の行列 A と m×l の行列 B を入力し、
# それらの積である n×l の行列 C を出力するプログラムを作成してください。
#  例） n = 3, m = 2 , l = 3の場合
#     1 2      1 2 1      1*1 + 2*0 1*2 + 2*3 1*1 + 2*2   1 8  5
# A = 0 3  B =        C = 0*1 + 3*0 0*2 + 3*3 0*1 + 3*2 = 0 9  6
#     4 5      0 3 2      4*1 + 5*0 4*2 + 5*3 4*1 + 5*2   4 23 14
import numpy as np


def calc_matrix_multiplication(args):
    n = 0
    m = 0
    l = 0
    matrix_a = np.array(())
    all_a_list = []
    all_b_list = []

    for i,val in enumerate(args):
        if i == 0:
            nml_list = [int(i) for i in val.split(' ')]
            n = nml_list[0]
            m = nml_list[1]
            l = nml_list[2]
        elif i >= 1 and i <= n:
            # locals()["list_%d" % i ] = [int(val) for val in val.split(' ')]
            a_list = [int(intval) for intval in val.split(' ')]
            all_a_list.append(a_list)
        elif i > n and i <= n + m:
            b_list = [int(intval) for intval in val.split(' ')]
            all_b_list.append(b_list)
        else:
            pass

    print np.array(all_a_list)
    print np.array(all_b_list)

    # AとBの積の計算
    print np.array(all_a_list).dot(np.array(all_b_list))

if __name__ == '__main__':
    args =[
        '3 2 3',
        '1 2',
        '0 3',
        '4 5',
        '1 2 1',
        '0 3 2'
        ]
    calc_matrix_multiplication(args)

    # test_ary = np.array([
    #     [1, 2],
    #     [0, 3],
    #     [4, 5]
    # ])
    # test2_ary = np.array([
    #     [9, 8],
    #     [7, 7],
    #     [8, 5]
    # ])
    # test_list = [1, 2]
    # test2_list = [3, 4]
    # print np.r_[test_ary, test2_ary]
    # print np.array([test_list, test2_list])

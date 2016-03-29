# -*- coding: utf-8 -*-
# 1 から n までの数の中から、重複無しで３つの数を選びそれらの合計が x となる
# 組み合わせの数を求めるプログラムを作成して下さい。

def calc_ansnum(m_n, s_n):
    ans_n = 0
    # range(i)[::-1]でデクリメントされる。[:X:]で、Xまでで完了。
    for i in range(m_n + 1)[:0:-1]:
        for j in range(i)[:0:-1]:
            for k in range(j)[:0:-1]:
                if i != j and j != k and k != i and i + j + k == s_n:
                    print '合計%i：%i+%i+%i' % (s_n, i, j, k)
                    ans_n += 1
    return ans_n

def howManyWays(vals):
    val_list = []
    max_num = 0
    sum_num = 0
    ans_num = 0

    for val in vals:
        val_list = [int(i) for i in val.split(' ')]
        max_num = val_list[0]
        sum_num = val_list[1]
        if max_num == 0 and sum_num == 0:
            print '完了'
            exit()
        else:
            ans_num = calc_ansnum(max_num, sum_num)
        print '解決方法は%i個' % (ans_num)

if __name__ == '__main__':
    args = ['18 26',
            '0 0'
            ]
    howManyWays(args)

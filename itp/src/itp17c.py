# -*- coding: utf-8 -*-
# 表計算を行う簡単なプログラムを作成します。
# 表の行数rと列数c、r × c の要素を持つ表を読み込んで、
# 各行と列の合計を挿入した新しい表を出力するプログラムを作成して下さい。

def add_sum(vals):
    row_num = 0
    column_num = 0
    val_list =[]
    row_sum = 0
    all_sum = 0
    row_list = []
    result_dict = {}

    for i,val in enumerate(vals):
        val_list = [int(vall) for vall in val.split(' ')]
        if i == 0:
            row_num = val_list[0]
            column_num = val_list[1]
            column_sum = [0] * column_num
        else:
            for j,data in enumerate(val_list):
                column_sum[j] += data
                row_list.append(data)
                row_sum += data
            row_list.append(row_sum)
            result_dict[i] = row_list
            all_sum += row_sum
            row_sum = 0
            row_list = []
    column_sum.append(all_sum)

    for key in result_dict.keys():
        print result_dict[key]
    print column_sum

if __name__ == '__main__':
    args = ['4 5',
            '1 1 3 4 5',
            '2 2 2 4 5',
            '3 3 0 1 1',
            '2 3 4 4 6'
            ]
    add_sum(args)

# -*- coding: utf-8 -*-
# n×m n×m の行列 A と、m×1m×1 の列ベクトルb を読み込み、
# A と b の積を出力するプログラムを作成してください。


def calc_matrix(args):
    # 初期化
    row_num = 0
    collum_num = 0
    matrix_a = {}
    collumn_b = {}
    result = 0

    # 変数セットと引数チェック
    for i,vals in enumerate(args):
        if i == 0 :
            val = vals.split(' ')
            if len(val) != 2:
                print 'arg missing'
                exit(' ERROR:第一引数が誤っています。')
            else:
                row_num = int(val[0])
                collum_num = int(val[1])
        elif i >= 1 and i <= row_num:
            if len(vals.split(' ')) != collum_num:
                print 'arg missing'
                exit(' ERROR:指定された列数に一致しません。')
            else:
                matrix_a[i] = vals

        elif i > row_num and i <= (row_num + collum_num):
            collumn_b[i - row_num] = int(vals)
        else:
            print '何かおかしい'

    # セットデータ確認
    print '行列Aの行数：', row_num,
    print '行列Bの列数：', collum_num
    print '行列A'
    for i,key in enumerate(matrix_a.keys()):
        print '[%i]' % (i) , matrix_a[key]
    print 'ベクトルB'
    for i,key in enumerate(collumn_b.keys()):
        print '[%i]' % (i), collumn_b[key]

    matrix_row = []
    #️ 行列とベクトルの積計算と表示
    for i, a_key in enumerate(matrix_a.keys()):
        matrix_row = [int(val) for val in matrix_a[a_key].split(' ')]
        for column, row in enumerate(matrix_row):
            result += int(matrix_row[column]) * collumn_b[column + 1]
        print '積:',
        print result
        result = 0

if __name__ == '__main__':
    print 'start'

    args = ['3 4',
            '1 2 0 1',
            '0 3 0 1',
            '4 1 1 0',
            1,
            2,
            3,
            0
            ]
    calc_matrix(args)
    print 'end'

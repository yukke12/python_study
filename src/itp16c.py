# -*- coding: utf-8 -*-
# Ａ大学は１フロア１０部屋、３階建ての公舎４棟を管理しています。公舎の入居・退去の情報を読み込み、
# 各部屋の入居者数を出力するプログラムを作成して下さい。
# n件の情報が与えられます。各情報では、４つの整数b, f, r, vが与えられます。
# これは、b棟f階のr番目の部屋にv人が追加で入居したことを示します。vが負の値の場合、v人退去したことを示します。

print "start"

import os

# 棟番号
tou_num = 1
# 階番号
kai_num = 1
# 部屋番号
hey_num = 1

tou_f = 0

fo = open("../data/itp16c.txt", "r")
fw = open("../data/itp16c_tmp.txt", "w")

# b:棟番号、f:階番号、r:左からの番目、v:人数
b, f, r, v = 4, 2, 5, 2

str_out = ""

for line in fo:
    len_r = len(line)
    for k in range(len_r):
        if (tou_num == b and kai_num == f and k == r - 1):
            str_out = str_out + str(v)
        else:
            str_out = str_out + line[k:k + 1]
    if(kai_num % 3 == 0):
        tou_num += 1
        kai_num = 1
        tou_f = 1
        str_out = str_out
        # + "################" + os.linesep
        # print "################"
    if tou_f == 0:
        kai_num += 1
        tou_f = 0
    else:
        kai_num = 1
        tou_f = 0

fw.write(str_out)

fw.close()
fo.close()

os.remove("../data/itp16c.txt")
os.rename("../data/itp16c_tmp.txt", "../data/itp16c.txt")

print str_out

print "end"

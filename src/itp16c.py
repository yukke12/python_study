# -*- coding: utf-8 -*-
# Ａ大学は１フロア１０部屋、３階建ての公舎４棟を管理しています。公舎の入居・退去の情報を読み込み、
# 各部屋の入居者数を出力するプログラムを作成して下さい。
# n件の情報が与えられます。各情報では、４つの整数b, f, r, vが与えられます。
# これは、b棟f階のr番目の部屋にv人が追加で入居したことを示します。vが負の値の場合、v人退去したことを示します。

print "start"

j = 0
fo = open("../data/itp16c.txt", "r")
fw = open("../data/itp16c_tmp.txt", "w")

for line in fo:
    j += 1
    print line.strip()
    if(j % 3 == 0):
        print "################"

fo.close()

print "end"

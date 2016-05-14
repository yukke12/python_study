# -*- coding: utf-8 -*-
# １つの整数 x を読み込み、それをそのまま出力するプログラムを作成して下さい。
# 0が来たら終わり。出力の形式は、Case i:x i番目の数字は、xを指す。

print "start"

i = 0
f = open('../data/itp13b.txt', 'r')

for line in f:
    i += 1
    if line == "0":
        break
    print "Case ", i, ":", line,
f.close()

print "end"

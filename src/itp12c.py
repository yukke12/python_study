# -*- coding: utf-8 -*-
# ３つの整数を読み込み、それらを値が小さい順に並べて出力するプログラムを作成して下さい。

print "start"

x = 12
y = 8
z = 10
a1 = 0
a2 = 0
a3 = 0

print "3つの数字は1つ目が", x, "、2つ目が", y, "、3つ目が", z

if x < y:
    a1 = x
    a2 = y
else:
    a1 = y
    a2 = x

x, y = a1, a2

print "x:", x, "、y:", y

if z < x:
    a1 = z
    a2 = x
    a3 = y
elif z < y:
    a2 = z
    a3 = y
else:
    a3 = z


print "並び替えると、", a1, a2, a3

print "end"

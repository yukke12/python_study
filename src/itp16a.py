# -*- coding: utf-8 -*-
# 与えられた数列を逆順に出力するプログラムを作成して下さい。

print "start"

a = "7931270243"
a_len = len(a)

print "入力は：", a
ans = ""

for i in range(a_len):
    ans = ans + str(a[a_len - i - 1: a_len - i])

print "出力は：", ans.strip()
print "end"

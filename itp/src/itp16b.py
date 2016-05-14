# -*- coding: utf-8 -*-
# 太郎が花子と一緒にトランプ遊びをしようとしたところ、52枚あるはずのカードが n 枚のカードしか手元にありません。
# これらの n 枚のカードを入力として、足りないカードを出力するプログラムを作成して下さい。

print "start"

f = open("../data/itp16b.txt", "r")
j = 0

for line in f:
    print line.strip()
f.close()

f = open("../data/itp16b.txt", "r")
for line in f:
    for x in range(len(line)):
        n = line[x: x + 1]
        if n == "0":
            if j == 0:
                print "スペードの", x + 1, "がありません。"
            if j == 1:
                print "ハートの", x + 1, "がありません。"
            if j == 2:
                print "ダイヤの", x + 1, "がありません。"
            if j == 3:
                print "ジャックの", x + 1, "がありません。"

    j = j + 1

print "end"

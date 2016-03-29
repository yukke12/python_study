# -*- coding: utf-8 -*-
# 与えられた英文に含まれる、各アルファベットの数を数えるプログラムを作成して下さい。
# なお、小文字と大文字は区別しません。


def calc_counting_char(strIn):
    lower_str = strIn.lower().replace(' ','').replace('.','')
    alfabet_dict = {}
    for one_char in lower_str:
        print one_char
    for i,char in enumerate([chr(i) for i in range(97,97+26)]):
        alfabet_dict[char] = 0
    print alfabet_dict

if __name__ == '__main__':
    args = 'This is a pen.'
    calc_counting_char(args)

# -*- coding: utf-8 -*-
# 与えられた文字列の小文字と大文字を入れ替えるプログラムを作成してください。


def Toggling_Cases(strSen):
    result = ''
    for i in range(len(strSen)):
        if strSen[i].islower():
            result += strSen[i].upper()
        else:
            result += strSen[i].lower()
    print result

if __name__ == '__main__':
    arg = 'fAIRoo, LATER, OccASIONALLY CLOUDY.'
    Toggling_Cases(arg)

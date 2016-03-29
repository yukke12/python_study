# -*- coding: utf-8 -*-
# 図のようなリング状の文字列 ss の任意の位置から、時計回りに連続した文字をいくつか選んで、
# 文字列 pp が作れるかを判定するプログラムを作成してください。


def judge_make_sentence(vals):
    main_sentence = ''
    search_target_sentence = ''
    for i,val in enumerate(vals):
        if i == 0:
            main_sentence = val
            search_target_sentence = main_sentence + main_sentence
        else:
            if search_target_sentence.find(val) > 0:
                print 'Yes'
            else:
                print 'No'


if __name__ == '__main__':
    args = ['vanceknowledgetoad',
            'advance',
            'advanced'
            ]
    judge_make_sentence(args)
# -*- coding: utf-8 -*-
# あなたの課題は、あるクラスの数学の成績を付けるプログラムを作成することです。
# プログラムは複数の学生のテストの点数を読み込みます。
# テストの点数は、中間試験の点数 m、期末試験の点数 f、再試験の点数 r で構成されています。
# 中間試験と期末試験は 50 点満点（m, f ≤ 50）、再試験は 100 点満点 （r ≤ 100）です。
# 試験を受けていない場合は点数を -1 とします。
# 以下の手順で成績が付けられます：
# 中間試験、期末試験のいずれかを欠席した場合成績は F。
# 中間試験と期末試験の合計点数が 80 以上ならば成績は A 。
# 中間試験と期末試験の合計点数が 65 以上 80 未満ならば成績は B。
# 中間試験と期末試験の合計点数が 50 以上 65 未満ならば成績は C。
# 中間試験と期末試験の合計点数が 30 以上 50 未満ならば成績は D。 ただし、再試験の点数が 50 以上ならば成績は C。
# 中間試験と期末試験の合計点数が 30 未満ならば成績は F。


def calc_grading(args):
    for val in args:
        score_list = [int(i) for i in val.split(' ')]
        if len(score_list) != 3:
            exit('引数が誤っています。')

        t_score = score_list[0]
        k_score = score_list[1]
        r_score = score_list[2]

        if t_score == -1 and k_score == -1:
            print '完了'
            return
        elif t_score == -1 or k_score == -1:
            if t_score == -1:
                print '成績：F 中間試験に欠席したため'
            elif k_score == -1:
                print '成績：F 期末試験に欠席したため'
        elif t_score + k_score < 30:
            print '成績：F 中間試験:%i, 期末試験:%i, 合計:%i' \
                  % (t_score, k_score, t_score + k_score)
        elif t_score + k_score >= 80:
            print '成績：A 中間試験:%i, 期末試験:%i, 合計:%i' \
                  % (t_score, k_score, t_score + k_score)
        elif t_score + k_score < 80 and t_score + k_score >= 65:
            print '成績：B 中間試験:%i, 期末試験:%i, 合計:%i' \
                  % (t_score, k_score, t_score + k_score)
        elif t_score + k_score < 65 and t_score + k_score >= 50:
            print '成績：C 中間試験:%i, 期末試験:%i, 合計:%i' \
                  % (t_score, k_score, t_score + k_score)
        elif t_score + k_score < 50 and t_score + k_score >= 30:
            if r_score >= 50:
                print '成績：C 中間試験:%i, 期末試験:%i, 合計:%i, 再試験:%i' \
                      % (t_score, k_score, t_score + k_score, r_score)
            else:
                print '成績：D 中間試験:%i, 期末試験:%i, 合計:%i, 再試験:%i' \
                      % (t_score, k_score, t_score + k_score, r_score)
        else:
            pass


if __name__ == '__main__':
    print 'start'
    args = ['40 42 -1',
            '20 30 -1',
            '0 2 -1',
            '40 30 -1',
            '-1 50 -1',
            '20 10 70',
            '30 -1 -1',
            '-1 -1 -1'
            ]
    calc_grading(args)
    print 'end'

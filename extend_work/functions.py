# -*- coding: utf-8 -*-
import sys
import traceback
import datetime


# 引数の初期値を指定することも可能。
def test(num1, num2, calc_kind='+'):
    try:
        if calc_kind == '+':
            return num1 + num2
        elif calc_kind == '-':
            return num1 - num2
        elif calc_kind == '*':
            return num1 * num2
        elif calc_kind == '/':
            return num1 / num2
    except:
        todaydetail = datetime.datetime.today()
        disp_date = todaydetail.strftime("%Y/%m/%d %H:%M:%S")
        print disp_date, '[WRN]', traceback.format_exc(sys.exc_info()[2])
    finally:
        pass


if __name__ == "__main__":
    todaydetail = datetime.datetime.today()
    disp_date = todaydetail.strftime("%Y/%m/%d %H:%M:%S")
    print disp_date, '[INF] start'
    a = test(10, 2)
    print a
    disp_date = todaydetail.strftime("%Y/%m/%d %H:%M:%S")
    print disp_date, '[INF] end'

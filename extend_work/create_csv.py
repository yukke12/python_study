# -*- coding: utf-8 -*-

import csv
import codecs


class CustomFormat(csv.excel):
    quoting = csv.QUOTE_ALL
#   delimiter = '\t'

if __name__ == "__main__":

    csvFile = codecs.open("./python.csv", "w", "shift_jis")
    writer = csv.writer(csvFile, CustomFormat())

    row = ("python", "-", "izm", "1")
    writer.writerow(row)

    rows = []
    rows.append(("python", "-", "izm", "2"))
    rows.append(("python", "-", "izm", "3"))
    rows.append(("p,y,t,h,o,n", "-", "i,z,m", "4"))
    writer.writerows(rows)

    csvFile.close()

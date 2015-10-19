# -*- coding: utf-8 -*-

# listクラスの継承


class TestExtends(list):

    def __init__(self):
        list.__init__(self)

    def append(self, value):
        list.append(self, value)
        print "added：" + str(value)


if __name__ == "__main__":

    test = TestExtends()
    test.append("python")
    test.append("-")
    test.append("izm")

    print "==============="

    for i in test:
        print i

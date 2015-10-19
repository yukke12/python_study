# -*- coding: utf-8 -*-


class TestClass:

    def __init__(self, code, name):
        self.code = code
        self.name = name

if __name__ == "__main__":

    classList = []
    classList.append(TestClass(1, "テスト１"))
    classList.append(TestClass(2, "テスト２"))

    for value in classList:
        print "===== class ====="
        print "code --> " + str(value.code)
        print "name --> " + value.name

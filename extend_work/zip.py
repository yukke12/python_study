# -*- coding: utf-8 -*-

import zipfile

if __name__ == "__main__":

    zipFile = zipfile.ZipFile("./compress_1.zip", "w", zipfile.ZIP_STORED)
    zipFile.write("./python.txt")
    zipFile.write("./python.csv")
    zipFile.close()

    zipFile = zipfile.ZipFile("./compress_2.zip", "w", zipfile.ZIP_DEFLATED)
    zipFile.write("./python.txt")
    zipFile.write("./python.csv")
    zipFile.close()

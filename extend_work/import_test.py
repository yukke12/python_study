# -*- coding: utf-8 -*-

import sys

# クラスの利用時に、まずはパスを追加。
# その後に、__init__.pyをおいた各ディレクトリを.でつないでインポートする。
sys.path.append("/Users/01001272/Documents/wk/python_study/extend_work")
import com.pythonism.calc

if __name__ == "__main__":

    print com.pythonism.calc.plusvalue(3, 1)

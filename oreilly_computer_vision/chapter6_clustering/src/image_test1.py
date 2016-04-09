# -*- coding: utf-8 -*-
import imtools
import pickle
from scipy.cluster.vq import *

if __name__ == '__main__':
    # 画像のリスト取得
    imlist = imtools.get_imlist('/usr/local/git_local/python_study/oreilly_computer_vision/data/PIXLEE-computer-vision-clustering/data/a_selected_thumbs')
    imnbr = len(imlist)
    print imnbr

    # モデルのファイルを読み込む
    with open('')

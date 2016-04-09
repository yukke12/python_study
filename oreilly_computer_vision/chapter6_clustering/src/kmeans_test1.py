# -*- coding: utf-8 -*-
"""
    Kmeans testing.
    test is doing below step.
    1) 100 float number and 2 dimentions generate by Gaussian distribution.
       first one is normal.
       second one is plus 5.
    2) do k-means, 1)'s feature using.
    3) plotting 2)'result.
"""

from scipy.cluster.vq import *
import numpy as np
import matplotlib.pyplot as plt


def drow_result(features, code, centroids):
    """
    abstruct:
        特徴量、クラスタ番号、

    :param features:特徴量
    :param code:属するクラスタ番号
    :param centroids:重心点
    :return:
    """

    plt.figure()
    # codeの中で0の要素だけ取得して、arrayにする。
    ndx = np.where(code == 0)[0]
    # plot(x, y, 指定)
    # o:小さい丸、*:星型、.:ひし形
    # デフォルト:青、r:赤、g:緑
    plt.plot(features[ndx, 0], features[ndx, 1],'*')
    ndx = np.where(code == 1)[0]
    plt.plot(features[ndx, 0], features[ndx, 1],'r.')
    plt.plot(centroids[:, 0], centroids[:, 1], 'go')
    plt.axis('off')
    plt.show()


def kmeans_clustering(features, k):
    """
    abstruct:
        k=2のkmeansを実行。
    :return:
        code:属するクラスタ番号
        centroids:重心座標
    """

    # do k-means clustering(k =2) centroids:重心点, variance:分散
    # scipyのkmeansは、20回試行して分散が最小になる重心点を採用する。
    centroids, variance = kmeans(features, k)

    # code:kmeansの種類の内、どれに割り当てられたか distance:重心からの距離
    code, distance = vq(features, centroids)
    # クラスタ1に割り当てられた数をカウント。
    # print np.count_nonzero((code > 0.5)*1)
    return code, centroids


def generate_gaussian_distribution(x):
    """
    abstruct:
        標準正規分布から引数分の浮動小数点の値を発生させる。
        1つ目の分布は、何も加工せず、2つ目の分布は5を足す。（5を足して、1つ目と2つ目がk-meansで別れやすくする）
    :param
        x: 発生させる乱数の数
    :return:
        features: 標準正規分布から発生させた全特徴量
    """

    # random.randn(100, 2): generate 100 number 2 dimension at Gaussian distribution random float number
    class1 = 1.5 * np.random.randn(100, 2)
    # 標準正規分布で発生させた100行2列に、5,5を足す。
    class2 = np.random.randn(100, 2) + np.array([5, 5])
    # 2つを結合
    features = np.vstack((class1, class2))
    return features


if __name__ == '__main__':
    # 標準正規分布で分布の異なる特徴量をvstackで縦に結合した2つの特徴量を結合したものを取得
    features = generate_gaussian_distribution(100)
    # 取得した特徴量で-kmeans(k=k個)のクラスタリングを実行。
    code, centroids = kmeans_clustering(features, 2)
    # features:特徴量、code:クラスタリング結果(0 or 1)
    drow_result(features, code, centroids)

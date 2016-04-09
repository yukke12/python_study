# -*- coding: utf-8 -*-
from scipy.cluster.vq import *
import numpy as np
import matplotlib.pyplot as plt


def drow_result(features, code, centroids):
    """

    :param features:
    :param code:
    :param centroids:
    :return:
    """

    plt.figure()
    ndx = np.where(code == 0)[0]
    print ndx
    plt.plot(features[ndx, 0], features[ndx, 1],'*')
    ndx = np.where(code == 1)[0]
    plt.plot(features[ndx, 0], features[ndx, 1],'r')
    plt.plot()

def kmeans_clustering():
    """
    abstruct:
        標準正規分布で100行2列のベクトルを2つ発生し、それをvstackで結合した特徴量にk=2のkmeansを実行。
    :return:
        features:特徴量
        code:属するクラスタ番号
        centroids:重心座標
    """
    # random.randn(100, 2): generate 100 number 2 dimension at Gaussian distribution random float number
    class1 = 1.5 * np.random.randn(100, 2)
    # 標準正規分布で発生させた100行2列に、5,5を足す。
    class2 = np.random.randn(100, 2) + np.array([5, 5])
    features = np.vstack((class1, class2))

    # do k-means clustering(k =2) centroids:重心点, variance:分散
    # scipyのkmeansは、20回試行して分散が最小になる重心点を採用する。
    centroids, variance = kmeans(features, 2)
    # print centroids

    # code:kmeansの種類の内、どれに割り当てられたか distance:重心からの距離
    code, distance = vq(features, centroids)
    # クラスタ1に割り当てられた数をカウント。
    # print np.count_nonzero((code > 0.5)*1)
    return features, code, centroids

if __name__ == '__main__':
    # 標準正規分布で発生させた100*2のベクトルをkmeans(k=2)でクラスタリングし、その実行結果を取得。
    # features:特徴量、code:クラスタリング結果(0 or 1)
    features, code = kmeans_clustering()
    drow_result(features, code, centroids)

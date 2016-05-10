# -*- coding: utf-8 -*-

import tensorflow as tf
import multiprocessing as mp

print [1, 1] + [2, 3]


core_num = mp.cpu_count()
print core_num
config = tf.ConfigProto(
    inter_op_parallelism_threads=core_num,
    intra_op_parallelism_threads=core_num )
sess = tf.Session(config=config)

print [1, 1]

hello = tf.constant('hello, tensorflow!')
print hello
print sess.run(hello)

a = tf.constant(10)
b = tf.constant(32)
print b
print sess.run(a+b)
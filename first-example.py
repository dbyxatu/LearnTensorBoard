# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 09:13:03 2017

@author: ASUS
"""

import tensorflow as tf

#定义一个简单的计算图，实现向量的加法的操作
input1 = tf.constant([1.0,2.0,3.0], name="input1")
input2 = tf.Variable(tf.random_uniform([3]), name="input2")
output = tf.add_n([input1, input2], name="add")

#生成一个写日志的writer,并将当前的Tensorflow计算图写入日志
writer = tf.summary.FileWriter("/path/to/log", tf.get_default_graph())
writer.close()


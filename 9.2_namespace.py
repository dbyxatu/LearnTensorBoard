# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 09:55:51 2017


通过命名空间来整理可视化效果图上的节点
@author: ASUS
"""

import tensorflow as tf

#with tf.variable_scope("foo"):
#    a = tf.get_variable("bar", [1])
#    print(a.name)
#    
#with tf.variable_scope("bar"):
#    b = tf.get_variable("bar", [1])
#    print(b.name)
    
with tf.name_scope("a"):
    a = tf.Variable([1])
    print(a.name)
    
    a = tf.get_variable("b", [1])
    print(a.name)
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 10:14:14 2017

@author: ASUS
"""

import tensorflow as tf

#with tf.variable_scope("foo"):
#    v = tf.get_variable("v",[1],initializer = tf.constant_initializer(1.0))
    
with tf.variable_scope("foo", reuse=True):
    v1 = tf.get_variable("v",[1])
    print(v==v1)
    print(v1.name)

v2 = tf.get_variable("v",[1])
print(v==v2)
print(v2.name)
    
#x = tf.constant()
#with tf.Session() as sess:  
#  sess.run(tf.global_variables_initializer())
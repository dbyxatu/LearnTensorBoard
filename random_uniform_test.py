# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 09:28:56 2017

@author: ASUS
"""
import tensorflow as tf
import numpy as np
with tf.Session() as sess:  
    print(sess.run(tf.random_uniform(  
        [3],dtype=tf.float32))) 
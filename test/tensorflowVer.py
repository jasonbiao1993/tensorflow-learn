# -*- coding: UTF-8 -*-
import os;
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2';
import tensorflow as tf;
print(tf.reduce_sum(tf.random.normal([1000, 1000])))
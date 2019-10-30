# -*- coding: UTF-8 -*-
import os;
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2';
# 引入Tensorflow库
import tensorflow as tf

hw = tf.constant('Hello world!')
print(hw)
print(hw.numpy())
print(hw.shape)
print(hw.dtype)


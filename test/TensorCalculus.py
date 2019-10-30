# 基本张量操作
# -*- coding: UTF-8 -*-
import os;
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2';
# 引入Tensorflow库
import tensorflow as tf

# 定义常量
a = tf.constant(3)
b = tf.constant(4)
c = tf.constant(5)
matrix1 = tf.constant([[1., 2.], [3., 4.]])
matrix2 = tf.constant([[5., 6.], [7., 8.]])
add = tf.add(a, b) # 求和
sub = tf.subtract(a, b) #求差
mul = tf.multiply(a, b) # 求乘
div = tf.divide(a, b) # 相除
mean = tf.reduce_mean([a, b, c]) # 求平均值
sum = tf.reduce_sum([a, b, c]) # 求和
matrix = tf.matmul(matrix1, matrix2) # 矩阵乘
print(add)
print(sub)
print(mul)
print(div)
print(mean)
print(sum)
print(matrix)

var = tf.Variable(3)
print(var)

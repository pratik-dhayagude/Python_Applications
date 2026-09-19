import tensorflow as tf


inputs = tf.constant([1.0,2.0,3.0])
weights = tf.constant([0.5,-0.2,0.8])
bias = tf.constant(0.1)

weighted_Sum = tf.reduce_sum(inputs*weights)+bias

print("WeightedSum:",weighted_Sum.numpy()) 
output = tf.sigmoid(weighted_Sum)

print("Sigmoid:",output.numpy())



import tensorflow as tf

tensor1 = tf.constant([10,20,30])
tensor2=tf.constant([1,2,3])


addition = tf.add(tensor1,tensor2)

print(addition)

sub= tf.subtract(tensor1,tensor2)
print(sub)
mul= tf.multiply(tensor1,tensor2)

print(mul)

div = tf.divide(tensor1,tensor2)

print(div)

square = tf.square(tensor1)

print(square)

Sum = tf.reduce_sum(tensor1)
print(Sum)


Min = tf.reduce_mean(tensor1)

print(Min)






import tensorflow as tf

weight = tf.Variable(5.0)

print("Initial Weight Value:",weight.numpy())

weight.assign(10.0)

print(weight.numpy())

weight.assign_add(2.5)
print(weight.numpy())

weight.assign_sub(1.5)

print(weight.numpy())



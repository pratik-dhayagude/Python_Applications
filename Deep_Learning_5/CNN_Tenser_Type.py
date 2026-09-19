import tensorflow as tf


# Scaler Tenser

Scaler_Tenser = tf.constant(11)


print(Scaler_Tenser)


# 1D Tenser

vector_Tensor = tf.constant([11,21,51,101])
print(vector_Tensor)

# 2D Tensor (Matrix)


matrix_tensor = tf.constant([[10,20,30],[40,50,60]])
print(matrix_tensor)

# 3D tensor

tensor_3d = tf.constant([
	[[1,2],[3,4]],
	[[5,5],[6,6]],
	[[7,8],[9,10]]
])
print(tensor_3d)

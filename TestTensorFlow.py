import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


observations = 1000

xs = np.random.uniform(low=-10, high=10, size=(observations, 1))
zs = np.random.uniform(10, 10, size=(observations, 1))

generated_inputs = np.column_stack((xs, zs))

noise = np.random.uniform(-1, 1, (observations, 1))

generated_targets = 2*xs - 3*zs + 5 + noise

np.savez('TF_Test', inputs=generated_inputs, targets=generated_targets)

input_size = 2
output_size = 1

inputs = tf.placeholder(tf.float32, [None, input_size])
targets = tf.placeholder(tf.float32, [None, output_size])


weights = tf.Variable(tf.random_uniform([input_size, output_size], minval=-0.1, maxval=0.1))

biases = tf.Variable(tf.random_uniform([output_size], minval=-0.1, maxval=0.1))

outputs = tf.matmul(inputs, weights) + biases

mean_loss = tf.losses.mean_squared_error(labels=targets, predictions=outputs) / 2.

optimize = tf.train.GradientDescentOptimizer(learning_rate=0.05).minimize(mean_loss)

sess = tf.InteractiveSession()

initialize = tf.global_variables_initializer()

sess.run(initialize)

training_data = np.load('TF_Test.npz')


for i in range(100):
    _, curr_loss = sess.run([optimize, mean_loss], feed_dict={inputs: training_data['inputs'],
                                                              targets: training_data['targets']})
    print(curr_loss)


out = sess.run([outputs], feed_dict={inputs: training_data['inputs']})
plt.plot(np.squeeze(out), np.squeeze(training_data['targets']))
plt.xlabel('Outputs')
plt.ylabel('Targets')
plt.show()
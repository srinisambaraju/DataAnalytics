import numpy as np
import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data

# This is how you read the data from the MNIST file

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)



input_size = 784
output_size = 10
hidden_layer_size = 50

# tf.reset_default_graph() clears the memory of all the variables left from previous runs (reset the computational)
# graph
tf.reset_default_graph()

inputs = tf.placeholder(tf.float32, [None, input_size])
targets = tf.placeholder(tf.float32, [None, output_size])

weights_1 = tf.get_variable("weights_1", [input_size, hidden_layer_size])
biases_1 = tf.get_variable("biases_1", [hidden_layer_size])

# Adding the activation function
# tf.nn is a module that contains neural network (nn) support. Among other things, it contains the most commonly
# used activation functions

# most commonly used activation functions are
# tf.nn.sigmoid
# tf.nn.tanh
# tf.nn.relu
# tf.nn.softmax

outputs_1 = tf.nn.relu(tf.matmul(inputs, weights_1) + biases_1)


weights_2 = tf.get_variable("weights_2", [hidden_layer_size, hidden_layer_size])
biases_2 = tf.get_variable("biases_2", [hidden_layer_size])
outputs_2 = tf.nn.relu(tf.matmul(outputs_1, weights_2) + biases_2)

weights_3 = tf.get_variable("weights_3", [hidden_layer_size, output_size])
biases_3 = tf.get_variable("biases_3", [output_size])
outputs = tf.nn.relu(tf.matmul(outputs_2, weights_3) + biases_3)

# Calculate the loss function for every output/target pair.
# The function used is the same as applying softmax to the last layer and then calculating cross entropy
# with the function we've seen in the lectures. This function, however, combines them in a clever way,
# which makes it both faster and more numerically stable (when dealing with very small numbers).
# Logits here means: unscaled probabilities (so, the outputs, before they are scaled by the softmax)
# Naturally, the labels are the targets.
loss = tf.nn.softmax_cross_entropy_with_logits(logits=outputs, labels=targets)

mean_loss = tf.reduce_mean(loss)

optimize = tf.train.AdamOptimizer(learning_rate=0.01).minimize(mean_loss)

# Prediction Accuracy - In what percentage of the cases did the algorithm assign the highest probability to the output
# that matched the target

out_equals_target = tf.equal(tf.arg_max(outputs, 1), tf.arg_max(targets, 1))

accuracy = tf.reduce_mean(tf.cast(out_equals_target, tf.float32))

sess = tf.InteractiveSession()
initializer = tf.global_variables_initializer()
sess.run(initializer)
batch_size = 100

# # batches = # samples / batch_size
batches_number = mnist.train._num_examples // batch_size


max_epochs = 15
# Keep track of the validation loss of the previous epoch.
# if the validation loss becomes increasing, we want to trigger early stopping.
# we initially set it at some arbitrarily high number to make sure we don't trigger it at first epoch
prev_validation_loss = 9999999.


# create a loop for epoch. Epoch_counter is a variable which automatically starts from 0.
for epoch_counter in range(max_epochs):
    # Keep track of the sum of batch losses in the epoch
    curr_epoch_loss = 0

    # Iterate over the batches in this epoch
    for batch_counter in range(batches_number):
        # Input batch and target batch are assigned values from the train data set, given a batch size
        input_batch, target_batch = mnist.train.next_batch(batch_size)
        # Run the optimization step and get the mean loss for this batch
        # Feed it with inputs and targets we just got from the train data set
        _, batch_loss = sess.run([optimize, mean_loss], feed_dict={inputs: input_batch, targets: target_batch})
        # Increment the sum of batch losses
        curr_epoch_loss += batch_loss
    # so far curr_epoch_loss contained the sum of all batches inside the epoch
    # we want to find the average batch losses over the whole epoch
    # The average batch loss is a good proxy for the current epoch loss
    curr_epoch_loss /= batches_number

    # At the end of each epoch, get the validation loss and accuracy
    # get the input batch and target batch from the validation data set
    input_batch, target_batch = mnist.validation.next_batch(mnist.validation._num_examples)
    # Run without the optimization step (simply forward propagate)
    validation_loss, validation_accuracy = sess.run([mean_loss, accuracy], feed_dict={inputs: input_batch, targets:
                                                                                      target_batch})
    # Print statistics for the current epochy
    # epoch counter +1, because epoch_counter automatically starts from 0, instead of 1
    # we format the losses with 3 digits after the dot
    # we format the accuracy in percentages for easier interpretation

    print('Epoch '+str(epoch_counter+1)+
          '. Mean loss: '+'{0:.3f}'.format(curr_epoch_loss) +
          '. Validation loss: '+'{0:.3f}'.format(validation_loss) +
          '. Validation accuracy: '+'{0:.2f}'.format(validation_accuracy * 100.)+'%')

    # Trigger early stopping if validation loss begins increasing.

    if validation_loss > prev_validation_loss:
        break
    # Store this epoch's validation loss to be used as previous validation loss in the next iteration.
    prev_validation_loss = validation_loss
print('End of training.')

input_batch, target_batch = mnist.test.next_batch(mnist.test._num_examples)
test_accuracy = sess.run([accuracy], feed_dict={inputs: input_batch, targets: target_batch})

# Test accuracy is a list with 1 value, so we want to extract the value from it, using x[0]
# Uncomment the print to see how it looks before the manipulation
# print (test_accuracy)
test_accuracy_percent = test_accuracy * 100.

# Print the test accuracy formatted in percentages
print('Test accuracy: '+'{0:.2f}'.format(test_accuracy_percent)+'%')

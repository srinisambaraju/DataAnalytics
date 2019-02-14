import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate random input data to train on

observations = 1000

xs = np.random.uniform(low=-10, high=10, size=(observations, 1))
zs = np.random.uniform(-10, 10, (observations, 1))

inputs = np.column_stack((xs, zs))

# create the targets we will aim at

noise = np.random.uniform(-1, 1, (observations, 1))

targets = 2*xs - 3*zs + 5 - noise

print(targets.shape)

# plot the training data
# In order to use the 3D plot, the objects should have a certain shape, so we reshape the targets.
# The proper method to use is reshape and takes as arguments the dimensions in which we want to fit the object.

targets = targets.reshape(observations, )

# Plotting according to the conventional matplotlib.pyplot syntax

# fig = plt.figure()

# A method allowing us to create the 3D Object

# ax = fig.add_subplot(111, projection='3d')

# chose the axes

# ax.plot(xs, zs, targets)

# set labels
# ax.set_xlabel('xs')
# ax.set_ylabel('zs')
# ax.set_zlabel('Targets')

# You can fiddle with the azim parameter to plot the data from different angles. Just change the value of azim=100
# to azim = 0 ; azim = 200, or whatever. Check and see what happens.

# ax.view_init(azim=100)

# So far we were just describing the plot. This method actually shows the plot.
# plt.show()

targets = targets.reshape(observations, 1)

init_range = 0.1

weights = np.random.uniform(-init_range, init_range, size=(2, 1))

biases = np.random.uniform(-init_range, init_range, size=1)

# print(weights)
# print(biases)

# set some small learning rate (denoted eta in the lecture)
# 0.02 is going to work quite well for our example.

learning_rate = 0.02

# Now its time to train the model.
# We iterate over our training data set 100 times. That works well with a learning rate of 0.02.
# The proper number of iteration is something comes from experience, but generally a lower learning rate would need more
# iterations while a higher learning rate would need less iterations
# Also we need to keep in mind that a high learning rate may cause the loss to diverge to infinity, instead of converge
# to 0

for i in range(100):
    # This is the linear equation model y = wx + b
    outputs = np.dot(inputs, weights) + biases
    # The deltas are the differences between the outputs and the targets
    # note that deltas here is a vector 100 X 1
    deltas = outputs - targets
    # we are considering the L2-norm Loss, but divided by 2, so it is consistent with the lectures
    # Moreover, we further divide it by the number of observations
    # This is a simple rescaling by a constant. We explained that this doesn't change the optimization logic,
    # as any function holding the basic property of being lower for better results, and higher for worse results
    # can be loss function

    loss = np.sum(deltas ** 2)/2 / observations

    # We print the loss function value at each step so we can observe whether it is decreasing as desired.
    # print(loss)

    # Another small trick is to scale the deltas the same ways as the loss function
    # In this way the learning rate is independent of the number of samples (observations).
    # Again, this doesn't change anything in principle, it simply makes it easier to pick a single learning rate
    # that can remain the same if we change the number of training samples (observations).
    # you can try solving the problem without rescaling to see how that works for you

    deltas_scaled = deltas / observations

    # Finally, we must apply the gradient descent update rules from the relevant lecture
    # The weights are 2X1, learning rate is 1X1(scalar), inputs are 1000X2, and deltas are 1000X1
    # We must transpose the inputs so that we get an allowed operation
    weights = weights - learning_rate * np.dot(inputs.T, deltas_scaled)
    biases = biases - learning_rate * np.sum(deltas_scaled)

    # The weights are updated in a linear algebraic way (a matrix minus another matrix)
    # The biases, however, are just a single number here, so we must transform the deltas into a scalar.
    # The two lines are both consistent wth the gradient descent methodology


print(weights, biases)

# plot lost outputs vs targets

plt.plot(outputs, targets)
plt.xlabel('Outputs')
plt.ylabel('Targets')
plt.show()


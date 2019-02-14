import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# This is the same logic but with a different learning rate 0.0001

observations = 1000000
low = -10
high = -low
xs = np.random.uniform(low=low, high=high, size=(observations, 1))
zs = np.random.uniform(low, high, size=(observations, 1))

inputs = np.column_stack((xs, zs))

noise = np.random.uniform(-1, 1, (observations, 1))

targets = 2*xs - 3*zs + 5 + noise

print(targets.shape)


learning_rate = 0.0001

init_range = 0.1

weights = np.random.uniform(-init_range, init_range, size=(2, 1))

biases = np.random.uniform(-init_range, init_range, size=1)

for i in range(100):

    outputs = np.dot(inputs, weights) + biases

    deltas = outputs - targets

    loss = deltas ** 2 / 2 / observations

    deltas_scaled = deltas / observations

    weights = weights - learning_rate * np.dot(inputs.T, deltas_scaled)

    biases = biases - learning_rate * np.sum(deltas_scaled)


print(weights, biases)

# For 1 million observations the graph plot is throwing an error

plt.plot(outputs, targets)
plt.xlabel('Outputs')
plt.ylabel('Targets')
plt.show()






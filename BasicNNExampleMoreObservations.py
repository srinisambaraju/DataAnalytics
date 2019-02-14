import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


observations = 1000
low = -10
high = -low
xs = np.random.uniform(low=low, high=high, size=(observations, 1))
zs = np.random.uniform(low, high, size=(observations, 1))
ys = np.random.uniform(low, high,size=(observations, 1))

inputs = np.column_stack((xs, zs, ys))

noise = np.random.uniform(-1, 1, (observations, 1))

targets = 2*xs - 3*zs + 5*ys + 5 + noise

print(targets.shape)

learning_rate = 0.02

init_range = 0.1

weights = np.random.uniform(-init_range, init_range, size=(3, 1))

biases = np.random.uniform(-init_range, init_range, size=1)

for i in range(100):

    outputs = np.dot(inputs, weights) + biases

    deltas = outputs - targets

    loss = deltas ** 2 / 2 / observations

    deltas_scaled = deltas / observations

    weights = weights - learning_rate * np.dot(inputs.T, deltas_scaled)

    biases = biases - learning_rate * np.sum(deltas_scaled)


print(weights, biases)

# plt.plot(outputs, targets)
# plt.xlabel('Outputs')
# plt.ylabel('Targets')
# plt.show()






import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

# 定义好初始权重
w = 1.0


# 定义预测函数，因为是要确定损失值随w的变化情况
# 后续会根据计算的梯度值来动态更新权重w
def forward(x):
    return x * w


# 定义损失函数的计算方式，使用梯度下降算法，计算数据集内所有样本的损失MSE
def cost(xs, ys):
    cost = 0
    for x, y in zip(xs, ys):
        y_pred = forward(x)
        cost += (y_pred - y) ** 2
    return cost / len(xs)


def gradient(xs, ys):
    grad = 0
    for x, y in zip(xs, ys):
        grad += 2 * x * (x * w - y)
    return grad / len(xs)


print('predict before training', 4, forward(4))

epochs = []
costs = []

for epoch in range(100):
    epochs.append(epoch)
    cost_val = cost(x_data, y_data)
    costs.append(cost_val)
    grad_val = gradient(x_data, y_data)
    w -= 0.01 * grad_val
    print('epoch:', epoch, 'w=', round(w, 2), 'loss=', round(cost_val, 2))
print('predict after training', 4, round(forward(4),2))

plt.plot(epochs, costs)
plt.ylabel('Cost')
plt.xlabel('Epoch')
plt.show()

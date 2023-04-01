import numpy as np
import matplotlib.pyplot as plt


def costFunctionJ(x, y, theta):
    '''代价函数'''
    m = np.size(x, axis=0)
    predictions = x * theta
    sqrErrors = np.multiply((predictions - y), (predictions - y))
    j = 1 / (2 * m) * np.sum(sqrErrors)
    return j


def gradientDescent(x, y, theta, alpha, num_iters):
    '''
    alpha为学习率
    num_iters为迭代次数
    '''
    m = len(y)
    n = len(theta)
    temp = np.mat(np.zeros([n, num_iters]))  # 用来暂存每次迭代更新的theta值，是一个矩阵形式
    j_history = np.mat(np.zeros([num_iters, 1]))  # #记录每次迭代计算的代价值
    for i in range(num_iters):  # 遍历迭代次数
        h = x * theta
        # temp[0,i] = theta[0,0] - (alpha/m)*np.dot(x[:,1].T,(h-y)).sum()
        # temp[1,i] = theta[1,0] - (alpha/m)*np.dot(x[:,1].T,(h-y)).sum()
        temp[:, i] = theta - (alpha / m) * np.dot(x[:, 1].T, (h - y)).sum()
        theta = temp[:, i]
        j_history[i] = costFunctionJ(x, y, theta)
    return theta, j_history, temp


x = np.mat(
    [1, 2000, 1, 2001, 1, 2002, 1, 2003, 1, 2004, 1, 2005, 1, 2006, 1, 2007, 1, 2008, 1, 2009, 1, 2010, 1, 2011, 1,
     2012, 1, 2013]).reshape(14, 2)
theta = np.mat([0, 2]).reshape(2, 1)
y = np.mat([2.000, 2.500, 2.900, 3.147, 4.515, 4.903, 5.365, 5.704, 6.853, 7.971, 8.561, 10.000, 11.280, 12.900]).reshape(14, 1)

# 求代价函数值
j = costFunctionJ(x, y, theta)
# print('代价值：',j)

plt.figure(figsize=(15, 5))
plt.subplot(1, 2, 1)
plt.scatter(np.array(x[:, 1])[:, 0], np.array(y[:, 0])[:, 0], c='r', label='real data')  # 画梯度下降前的图像
plt.plot(np.array(x[:, 1])[:, 0], x * theta, label='test data')
plt.legend(loc='best')
plt.title('before')

theta, j_history, temp = gradientDescent(x, y, theta, 0.01, 100)
print('最终j_history值：\n', j_history[-1])
print('最终theta值：\n', theta)
print('每次迭代的代价值：\n', j_history)
print('theta值更新历史：\n', temp)

plt.subplot(1, 2, 2)
plt.scatter(np.array(x[:, 1])[:, 0], np.array(y[:, 0])[:, 0], c='r', label='real data')  # 画梯度下降后的图像
plt.plot(np.array(x[:, 1])[:, 0], x * theta, label='predict data')
plt.legend(loc='best')
plt.title('after')
plt.show()

import numpy as np

# 输入数据
X = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013]
Y = [2.000, 2.500, 2.900, 3.147, 4.515, 4.903, 5.365, 5.704, 6.853, 7.971, 8.561, 10.000, 11.280, 12.900]


def linear_regression(X, Y, learning_rate=0.01, num_iterations=100):
    # 转换X和Y为numpy数组
    X = np.array(X)
    Y = np.array(Y)

    # 参数初始化
    n_samples = len(X)
    slope = 0
    intercept = 0
    # costs = []

    # 梯度下降迭代
    for i in range(num_iterations):
        # 计算预测值
        Y_pred = slope * X + intercept
        print(Y, Y_pred)

        # # 计算误差
        # cost = (1 / n_samples) * np.sum((Y_pred - Y) ** 2)
        # costs.append(cost)

        # 计算梯度
        D_slope = (2 / n_samples) * np.sum(X * (Y_pred - Y))
        D_intercept = (2 / n_samples) * np.sum(Y_pred - Y)

        # 更新参数
        slope -= learning_rate * D_slope
        intercept -= learning_rate * D_intercept

    return slope, intercept


class LinearRegression:
    def __init__(self, learning_rate=0.01, num_iterations=1000, regularization_factor=0.01):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.regularization_factor = regularization_factor
        self.weight = None
        self.bias = None

    def fit(self, X, Y):
        # 参数初始化
        n_samples = len(X)
        self.weight = 0.0
        self.bias = 0.0
        costs = []

        # 梯度下降迭代
        for i in range(self.num_iterations):
            # 计算预测值
            Y_pred = [self.weight * x + self.bias for x in X]

            # 计算误差
            cost = (1/n_samples) * sum([(y_pred - y)**2 for y_pred, y in zip(Y_pred, Y)])
            cost += (self.regularization_factor/n_samples) * (self.weight**2)
            costs.append(cost)

            # 计算梯度
            dW = (1/n_samples) * sum([x * (y_pred - y) for x, y_pred, y in zip(X, Y_pred, Y)])
            dW += (2*self.regularization_factor/n_samples) * self.weight
            db = (1/n_samples) * sum([y_pred - y for y_pred, y in zip(Y_pred, Y)])

            # 更新参数
            self.weight -= self.learning_rate * dW
            self.bias -= self.learning_rate * db

        return costs

    def predict(self, X):
        Y_pred = [self.weight * x + self.bias for x in X]
        return Y_pred


if __name__ == '__main__':
    # print(linear_regression(a, b))
    so = LinearRegression()
    print(so.fit(X, Y))

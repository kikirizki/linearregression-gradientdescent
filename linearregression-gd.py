__author__ = 'Kiki Rizki Arpiandi'
import numpy as np
import random
import matplotlib.pyplot as plt


class model:
    def __init__(self, y):
        self.y = y
        self.x = np.arange(0, len(self.y), 1)
        self.theta0 = random.randrange(-5, 5, 1)
        self.theta1 = random.randrange(-5, 5, 1)

    def set(self, theta0, theta1):
        self.theta0 = theta0
        self.theta1 = theta1

    def h(self, x):
        return (self.theta1 * x) + self.theta0

    def J(self):
        return np.average((self.h(self.x) - self.y) ** 2) / 2

    def delta_h_delta_theta0(self):
        return np.average((self.h(self.x) - self.y))

    def delta_h_delta_theta1(self):
        return np.average((self.h(self.x) - self.y) * self.x)

    def plot(self):
        plt.plot(self.x, reg.h(self.x))
        plt.plot(self.x, self.y, 'ro')
        plt.show()

    def do_gradient_descent(self):
        error = 0
        while (abs(reg.J() - error) > 0.0000001):
            error = reg.J()
            temp0 = self.theta0 - 0.01 * reg.delta_h_delta_theta0()
            temp1 = self.theta1 - 0.01 * reg.delta_h_delta_theta1()
            self.theta0 = temp0
            self.theta1 = temp1


data_example = np.array([1., 2., 3., 4., 5., 6.])
reg = model(data_example)
reg.do_gradient_descent()
reg.plot()

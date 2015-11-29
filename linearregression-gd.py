__author__ = 'Kiki Rizki Arpiandi'
import numpy as np
import random
import matplotlib.pyplot as plt


class model:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.theta0 = random.randrange(-5, 5, 1)
        self.theta1 = random.randrange(-5, 5, 1)

    def set(self, theta0, theta1):
        self.theta0 = theta0
        self.theta1 = theta1

    def h(self, x):
        return (self.theta1 * x) + self.theta0

    def J(self):
        return np.average((self.h(self.x) - self.y) ** 2) / 2

    def delta_theta0(self):
        return np.average((self.h(self.x) - self.y))

    def delta_theta1(self):
        return np.average((self.h(self.x) - self.y) * self.x)

    def plot(self):
        plt.plot(self.x, reg.h(self.x))
        plt.plot(self.x, self.y, 'ro')
        plt.show()


waktu = np.arange(1, 21, 1)
curahhujan = np.array([2., 3., 4., 2., 7., 5., 7., 8., 9., 10., 23., 34., 43., 30., 45., 43., 32., 32., 38., 45.])
reg = model(waktu, curahhujan)
theta0 = 2.
theta1 = 2.
for i in range(1000):
    theta0 = theta0 - 0.01 * reg.delta_theta0()
    theta1 = theta1 - 0.01 * reg.delta_theta1()
    reg.set(theta0, theta1)
reg.plot()

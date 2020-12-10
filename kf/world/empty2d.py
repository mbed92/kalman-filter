import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

from .IWorld import IWorld


class EmptyWorld2D(IWorld):
    def __init__(self, width: int, height: int, show_path: bool = True):
        super().__init__(width, height, show_path)
        self.ndim = 2

    def update_location(self, agent_location, **kwargs):
        assert len(agent_location) == self.ndim
        color = kwargs["color"] if hasattr(kwargs, "color") else "blue"
        self.ax.scatter(agent_location[0], agent_location[1], c=color)

    def add_gaussian_uncertainty(self, mean, variance, rgb):
        # p = gaussian_kernel_2d(100, mean, variance)
        # self.ax.pcolormesh(p[0], p[1], p[2], cmap=cmap)
        e = Ellipse(xy=mean, width=variance[0], height=variance[1])
        e.set_facecolor(rgb)
        self.ax.add_artist(e)


def gaussian_function(x, mean, sigma):
    return np.exp(-np.power(x - mean, 2.) / (2 * np.power(sigma, 2.)))


def gaussian_kernel_2d(size, mean, sigma):
    xx = np.linspace(mean[0] - sigma[0], mean[0] + sigma[0], size)
    yy = np.linspace(mean[1] - sigma[1], mean[1] + sigma[1], size)

    x1 = [gaussian_function(x, mean[0], sigma[0]) for x in xx]
    x2 = [gaussian_function(y, mean[1], sigma[1]) for y in yy]
    z = np.outer(x1, x2)
    z = 255. * (z - z.min()) / (z.max() - z.min())

    xx, yy = np.meshgrid(xx, yy)
    return np.stack([xx, yy, z])

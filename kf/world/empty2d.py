import numpy as np
from matplotlib.patches import Ellipse

from .IWorld import IWorld


class EmptyWorld2D(IWorld):
    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self.ndim = 2
        self.v_vec = None

    def plot_location(self, agent_location, agent_velocity=None, **kwargs):
        assert len(agent_location) == self.ndim
        color = kwargs["color"] if "color" in kwargs else "blue"
        self.ax.scatter(agent_location[0], agent_location[1], c=color)

        # draw a vector of the predicted velocity
        if agent_velocity is not None:
            self.v_vec = agent_velocity
            x, y, dx, dy = agent_location[0], agent_location[1], agent_velocity[0], agent_velocity[1]
            self.ax.arrow(x, y, dx, dy, color=color)

    def plot_gaussian_uncertainty(self, mean, variance, **kwargs):
        assert variance.shape[0] == mean.shape[0]
        assert variance.shape[1] == self.ndim
        color = kwargs["color"] if "color" in kwargs else "blue"

        # visualize the gaussian uncertainty as an ellipse rotated w.r.t. the velocity vector
        for i in range(variance.shape[0]):
            e = Ellipse(xy=mean, width=variance[i][0], height=variance[i][0])
            e.set_facecolor(color)
            self.ax.add_artist(e)

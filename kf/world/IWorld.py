import matplotlib.pyplot as plt


class IWorld(object):
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height

        self.figure = plt.figure(figsize=[width, height])
        self.ax = self.figure.gca()
        self.ax.set_xlim([0, width])
        self.ax.set_ylim([-height, height])

    def plot_location(self, agent_location, agent_velocity, **kwargs):
        raise NotImplementedError("Implement that method.")

    def plot_gaussian_uncertainty(self, mean, variance, **kwargs):
        raise NotImplementedError("Implement that method.")

    def show(self):
        self.figure.show()

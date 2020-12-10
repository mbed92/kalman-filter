import matplotlib.pyplot as plt


class IWorld(object):
    def __init__(self, width: int, height: int, show_path: bool = True):
        self.w = width
        self.h = height
        self.show_path = show_path

        self.figure = plt.figure(figsize=[width, height])
        self.ax = self.figure.gca()
        self.ax.set_xlim([-width, width])
        self.ax.set_ylim([-height, height])

    def update_location(self, agent_location):
        raise NotImplementedError("Implement that method.")

    def add_gaussian_uncertainty(self, mean, variance, rgb):
        raise NotImplementedError("Implement that method.")

    def show(self):
        self.figure.show()

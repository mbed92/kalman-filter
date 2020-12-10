import numpy as np


class IKalman(object):
    def __init__(self, ndim: int):
        self.ndim = ndim
        self.external_motion_vector = np.array([[0., 0.], [0, 0.]])
        self.next_state_matrix = np.array([[1., 1.], [0, 1.]])
        self.state_matrix = np.array([[1., 0.]])
        self.num_observables = self.state_matrix.sum().astype(int)
        self.measurement_uncertainty = np.ones(self.num_observables)

    def update(self, *args):
        raise NotImplementedError("Implement that method.")

    def predict(self, *args):
        raise NotImplementedError("Implement that method.")

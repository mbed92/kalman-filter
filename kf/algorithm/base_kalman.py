import numpy as np

from .IKalman import IKalman


class KalmanFilter(IKalman):

    def __init__(self, ndim: int):
        super().__init__(ndim)
        self.identity = np.eye(self.ndim)

    def update(self, state: np.ndarray, uncertainty: np.ndarray, measurement: np.ndarray):
        # compute an observation matrix
        y = np.asarray([[measurement]]) - self.state_matrix @ state
        S = self.state_matrix @ uncertainty @ self.state_matrix.T
        S += self.measurement_uncertainty
        K = uncertainty @ self.state_matrix.T @ np.linalg.inv(S)

        # update a state and an uncertainty
        new_state = state + K @ y
        new_uncertainty = (self.identity - K @ self.state_matrix) @ uncertainty
        return new_state, new_uncertainty

    def predict(self, state: np.ndarray, uncertainty: np.ndarray):
        new_state = self.next_state_matrix @ state + self.external_motion_vector
        new_uncertainty = self.next_state_matrix @ uncertainty @ self.next_state_matrix.T
        return new_state, new_uncertainty

import numpy as np


class IAlgorithm(object):
    def __init__(self,
                 initial_uncertainty,
                 observables_selection_matrix,
                 measurement_uncertainty):

        # make sure the dimensions of input matrices match
        iu_r = np.shape(initial_uncertainty)
        s_r = np.shape(observables_selection_matrix)
        assert iu_r[0] == s_r[0]
        r = np.rank(initial_uncertainty)

        # set matrices
        self.initial_uncertainty = initial_uncertainty
        self.observables_selection_matrix = observables_selection_matrix
        self.measurement_uncertainty = measurement_uncertainty

        # set defaults
        self.external_motion_vec = np.zeros_like(observables_selection_matrix)
        self.next_state_mat = np.eye(r)

    def update(self, *args):
        raise NotImplementedError("Implement that method.")

    def predict(self):
        raise NotADirectoryError("Implement that method.")

    @staticmethod
    def std_spec():
        return {
            'initial_uncertainty': np.array([[1000., 0.], [0., 1000.]]),
            'sensor_uncertainty': np.array([[1.]]),
            'observables_selection_matrix': np.array([[1., 0.]])
        }

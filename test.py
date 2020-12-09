import numpy as np

import kf

# # initialize the kalman filter
# state = np.asarray([[0., 0], [0., 0]])
# uncertainty = np.eye(state.ndim) * 9999
# measurements = np.asarray([[1, 1], [2, 2], [3, 3]])
# algo = kf.algorithm.base_kalman.KalmanFilter(ndim=2)
#
# initialize the world
env = kf.world.EmptyWorld2D(3, 3)
env.update_location([1, 1])
env.add_gaussian_uncertainty([1, 1], [4, 4])
env.show()

#
# # start moving in the world
# for measurement in measurements:
#     state, uncertainty = algo.update(state, uncertainty, measurement)
#     state, uncertainty = algo.predict(state, uncertainty)
#
# print(state, '\n', uncertainty)

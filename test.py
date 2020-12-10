import numpy as np

import kf

# initialize the kalman filter
state = np.asarray([[0., 0], [0., 0]])
uncertainty = np.eye(state.ndim) * 9999
measurements = np.asarray([[1, 1], [2, 2], [3, 3]])
algo = kf.algorithm.base_kalman.KalmanFilter(ndim=2)

# initialize the world
env = kf.world.EmptyWorld2D(10, 10)


# start moving in the world
for measurement in measurements:
    state, uncertainty = algo.update(state, uncertainty, measurement)
    state, uncertainty = algo.predict(state, uncertainty)

    xy = state[0, 0, 1], state[0, 0, 0]
    unc = np.diag(uncertainty) / 1000
    env.update_location(xy)
    env.add_gaussian_uncertainty(xy, unc)
    env.show()
    env.clear()

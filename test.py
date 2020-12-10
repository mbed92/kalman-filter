import numpy as np

import kf

# initialize the kalman filter
algo = kf.algorithm.base_kalman.KalmanFilter(ndim=2)
state = np.asarray([[0., 0.], [0., 0.]])
uncertainty = np.eye(state.ndim) * 10.
x = np.linspace(0, 10, 10)
y = np.sin(x)
measurements = np.stack([x, y]).T

# initialize the world
C1, C2 = [0.0, 0.5, 0.0, 0.2], [0.5, 0.0, 0.0, 0.2]
env = kf.world.EmptyWorld2D(5, 15)

# start moving in the world
for measurement in measurements:
    state, uncertainty = algo.update(state, uncertainty, measurement)
    state, uncertainty = algo.predict(state, uncertainty)

    xy = state[0, 0, 1], state[0, 0, 0]
    unc = np.diag(uncertainty)
    env.update_location(xy)
    env.add_gaussian_uncertainty(xy, unc, C2)

env.show()


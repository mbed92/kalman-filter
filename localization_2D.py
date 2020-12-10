'''
A very simple example of a localization using Kalman Filter.
Author: Michał Bednarek
'''

import numpy as np

import kf

# initialize the Kalman filter
algo = kf.algorithm.base_kalman.KalmanFilter(ndim=2)
state = np.asarray([[0., 0.], [0., 0.]])            # position and velocity of a moving point
uncertainty = np.eye(state.ndim) * 15.              # initial uncertainty
x = np.linspace(0, 14, 30)                          # path (measurements)
y = np.cos(0.5 * x)
measurements = np.stack([x, y]).T
env = kf.world.EmptyWorld2D(15, 5)                  # initialize the world

# start moving in the world
for measurement in measurements:
    state, uncertainty = algo.update(state, uncertainty, measurement)
    state, uncertainty = algo.predict(state, uncertainty)

    pos = state[0, :]     # pick the location (blue points)
    vel = state[1, :]     # pick the velocity (red arrows)

    env.plot_gaussian_uncertainty(pos, uncertainty, color=[0.2, 0.2, 0.2, 0.2])
    env.plot_location(measurement, None, color='red')
    env.plot_location(pos, vel, color='blue')

env.show()
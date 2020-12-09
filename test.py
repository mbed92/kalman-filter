import numpy as np


# Implement the filter function below
def kalman_filter(x, P):
    for n in range(len(measurements)):
        # measurement update
        z = np.array([[measurements[n]]])  # put measurments into the form of a 1x1 matrix
        y = z - H @ x  # compute an error between a new state and measurment
        S = H @ P @ H.transpose() + R  # measurement uncertainty update
        K = P @ H.transpose() @ np.linalg.inv(S)  # Observation matrix
        x = x + K @ y  # state update
        P = (I - K @ H) @ P  # uncertainty update (entropy decreases)

        # prediction
        x = F @ x + u  # state equations update
        P = F @ P @ F.transpose()  # state uncertainty update (entropy increases)

    return x, P


############################################
### use the code below to test your filter!
############################################

measurements = [
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2],
]

x = np.array([[0., 0., 0.], [0., 0., 0.]])  # initial state (location and velocity)
P = np.array([[1000., 0.], [0., 1000.]])  # initial uncertainty
u = np.array([[0.], [0.]])  # external motion
F = np.array([[1., 1.], [0, 1.]])  # next state function
H = np.array([[1., 0.]])  # measurement function (observables selection)
R = np.array([[1.]])  # measurement uncertainty
I = np.array([[1., 0.], [0., 1.]])  # identity matrix

print(kalman_filter(x, P))

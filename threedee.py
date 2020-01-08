import numpy as np
from numpy import cos as cos, sin as sin, pi as pi
import scipy

from scipy import spatial


def rotateY(p, a):
    x = p[0]
    y = p[1]
    z = p[2]

    rm = np.array([
        [cos(a), 0, sin(a)],
        [0, 1, 0],
        [-sin(a), 0, cos(a)]
    ])

    point = np.array([[x], [y], [z]])

    t = rm.dot(point)
    # print(round(float(t[0]), 2), round(float(t[2]), 2))

    return t

rotateY([1,2,3],4)

def project(p,w,h):
    x = p[0]
    y = p[1]
    z = p[2]
    # prj = np.array([
    #     [z,0,0],
    #     [0,z,0]]
    mz = 1 / (20 - z)
    pm = np.array([
        [mz, 0, 0],
        [0, mz, 0]])

    prj = pm.dot(p)
    # prj[0] += w/2
    # prj[1] += h/2
    prj = prj*18

    #print(prj)
    return(prj)



if __name__ == "__main__":
    points = [
        [-2, -2, -2],
        [2, -2, -2],
        [2, 2, -2],
        [2, 2, 2],
        [-2, -2, 2],
        [-2, -2, 2],
        [-2, 2, -2],
        [2, -2, 2],
        ]
    a = 0
    for q in range(100):

        for x,i in enumerate(points):
            project(rotateY(i, a),0, 0)
        a += 0.1


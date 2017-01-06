from nose.tools import assert_equal
import numpy as np
from matplotlib import pyplot as plt
from ..animateboids import AnimateBoids

"""
class AnimateBoids(object):
    def __init__(self, positions, velocities):
        self.positions = positions
        self.velocities = velocities

    def update_boids(self, positions, velocities):
        up_date = UpdateBoids(positions, velocities)
        up_date.to_middle()
        up_date.away_from()
        up_date.match_speed()
        up_date.move_velocities()

    def animate(self, frame, scatter):
        self.update_boids(self.positions, self.velocities)
        scatter.set_offsets(zip(self.positions[0], self.positions[1]))

    def display(self):
        figure=plt.figure()
        axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
        scatter=axes.scatter(self.positions[0], self.positions[1])
        anim = animation.FuncAnimation(figure, self.animate, fargs=[scatter], frames=50, interval=50)
        plt.show()
"""

"""
#code used to create positions and velocities randomly initally
#code known to work used instead of calling a class to avoid
#changes in that class causing an error in this testing
def new_flock(count, lower_limits, upper_limits):
    width=upper_limits-lower_limits
    return (lower_limits[:,np.newaxis] + np.random.rand(2, count)*width[:,np.newaxis])

positions = new_flock(10, np.array([0.0, 0.0]), np.array([10.0, 10.0]))
velocities = new_flock(10,np.array([0.0, 0.0]), np.array([10.0, 10.0]))
"""
positions = np.array([[0.57060007, 4.72023739, 9.2721358, 7.93680601, 4.28602204, 5.48081302, 3.96498288, 1.73486068,9.99097606, 1.96189901], [ 9.49748595, 4.9919118, 7.68153802, 4.31255511, 4.12122648, 7.45132605, 0.33013738, 8.77902153, 3.30667064, 4.1014684]])

velocities = np.array([[2.68064552, 0.9713136, 7.00683802, 2.2028798, 9.41221644, 2.03085767, 6.35253961,8.30404115, 4.96033289, 3.06305922], [1.62756439, 9.19521275, 4.6318786, 3.51823417, 6.0947243, 2.31391316, 5.18996174, 1.06550607, 0.70059282, 8.19460193]])


ab = AnimateBoids(positions, velocities)

def test_update_boid():
    #simple test to isolate update_boids and test it with pre-defined working inputs to look for failure
    ub = ab.update_boids(positions, velocities)
    assert_equal(ub, None)

test_update_boid()


axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(positions[0], positions[1])

def test_animate(scatter):
    #simple test to isolate animate and test it with pre-defined working inputs to look for failure
    a = ab.animate(1,scatter)
    assert_equal(a, None)

test_animate(scatter)


def test_display():
    #simple test to isolate display and test it with pre-defined working inputs to look for failure
    #will (if working) display two plots this is not a issue just caused by the method that its being called by
    d = ab.display()
    assert_equal(d, None)


test_display()
























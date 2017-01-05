from nose.tools import assert_almost_equal, assert_equal, assert_less, assert_greater
import numpy as np
from newboids import NewBoids

"""
class NewBoids(object):
    def __init__(self, num_boids):
        self.num_boids = num_boids
    
    def new_flock(self, count, lower_limits, upper_limits):
        #returns two colums of random numbers between the limits
        #for ll=[a,b] & ul=[c,d], colum1 is between a-c and 2 is b-d
        width=upper_limits-lower_limits
        return (lower_limits[:,np.newaxis] + np.random.rand(2, count)*width[:,np.newaxis])

    def return_boids(self):
        positions = self.new_flock(self.num_boids, np.array([-450, 300.0]), np.array([50.0, 600.0]))
        velocities = self.new_flock(self.num_boids,np.array([0, -20.0]), np.array([10.0, 20.0]))
        return (positions, velocities)

"""
nb = NewBoids(10)

def test_new_flock():
    #tests to see if the shape and limits are correct when calling the function
    nf = nb.new_flock(10, np.array([0, 10]), np.array([5, 15]))
    
    assert_equal(nf.shape, (2, 10))
    
    for i in range(10): #check range (to 1dp)
        assert_greater(nf[0][i],-0.1)
        assert_less(nf[0][i],5.1)

        assert_greater(nf[1][i],9.9)
        assert_less(nf[1][i],15.1)

test_new_flock()

def test_return_boids():
    #checks that the currect shape is returned
    rb = nb.return_boids()
    assert_equal(rb[0].shape,(2, 10))
    assert_equal(rb[1].shape,(2, 10))

test_return_boids()

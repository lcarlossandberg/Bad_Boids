import random
import numpy as np

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



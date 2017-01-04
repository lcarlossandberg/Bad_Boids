from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np

Birds = 50 #number of birds in the simulation


def new_flock(count, lower_limits, upper_limits):
    #returns two colums of random numbers between the limits
    #for ll=[a,b] & ul=[c,d], colum1 is between a-c and 2 is b-d
    width=upper_limits-lower_limits
    return (lower_limits[:,np.newaxis] + np.random.rand(2, count)*width[:,np.newaxis])

positions = new_flock(Birds, np.array([-450, 300.0]), np.array([50.0, 600.0]))
velocities = new_flock(Birds,np.array([0, -20.0]), np.array([10.0, 20.0]))

class UpdateBoids(object):
    def __init__(self, positions, velocities):
        self.positions = positions
        self.velocities = velocities

    
        # Fly towards the middle
        strength_of_atraction = 0.01
        middle_of_flock = np.mean(positions, 1)
        direction_to_middle = positions - middle_of_flock[:, np.newaxis]
        velocities -= direction_to_middle*strength_of_atraction

        # Fly away from nearby boids
        separations = positions[:,np.newaxis,:] - positions[:,:,np.newaxis]
        squared_displacements = separations * separations
        square_distances = np.sum(squared_displacements, 0)
        alert_distance = 100
        far_away = square_distances > alert_distance
        separations_if_close = np.copy(separations)
        separations_if_close[0,:,:][far_away] =0
        separations_if_close[1,:,:][far_away] =0
        velocities += np.sum(separations_if_close,1)

        # Try to match speed with nearby boids
        velocity_separation = velocities[:,np.newaxis,:] - velocities[:,:,np.newaxis]
        formation_flying_distance = 10000
        formation_flying_strength = 0.125
        very_far=square_distances > formation_flying_distance
        velocity_separation_if_close = np.copy(velocity_separation)
        velocity_separation_if_close[0,:,:][very_far] =0
        velocity_separation_if_close[1,:,:][very_far] =0
        velocities -= np.mean(velocity_separation_if_close, 1) * formation_flying_strength
    
        # Move according to velocities
        positions += velocities


figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(positions[0],positions[1])

def animate(frame):
    UpdateBoids(positions, velocities)
    scatter.set_offsets(zip(positions[0],positions[1]))

anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
















from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np

class NewBoids(object):
    def __init__(self, birds):
        self.birds = birds
    
    def new_flock(self, count, lower_limits, upper_limits):
        #returns two colums of random numbers between the limits
        #for ll=[a,b] & ul=[c,d], colum1 is between a-c and 2 is b-d
        width=upper_limits-lower_limits
        return (lower_limits[:,np.newaxis] + np.random.rand(2, count)*width[:,np.newaxis])

    def return_boids(self):
        #Birds = 50 #number of birds in the simulation
        positions = self.new_flock(self.birds, np.array([-450, 300.0]), np.array([50.0, 600.0]))
        velocities = self.new_flock(self.birds,np.array([0, -20.0]), np.array([10.0, 20.0]))
        return (positions, velocities)

class UpdateBoids(object):
    def __init__(self, positions, velocities):
        self.positions = positions
        self.velocities = velocities

    def to_middle(self):
        # Fly towards the middle
        strength_of_atraction = 0.01
        middle_of_flock = np.mean(self.positions, 1)
        direction_to_middle = self.positions - middle_of_flock[:, np.newaxis]
        self.velocities -= direction_to_middle*strength_of_atraction

    def away_from(self):
        # Fly away from nearby boids
        separations = self.positions[:,np.newaxis,:] - self.positions[:,:,np.newaxis]
        squared_displacements = separations * separations
        square_distances = np.sum(squared_displacements, 0)
        alert_distance = 100
        far_away = square_distances > alert_distance
        separations_if_close = np.copy(separations)
        separations_if_close[0,:,:][far_away] = 0
        separations_if_close[1,:,:][far_away] = 0
        self.velocities += np.sum(separations_if_close,1)

    def match_speed(self):
        # Try to match speed with nearby boids
        velocity_separation = self.velocities[:,np.newaxis,:] - self.velocities[:,:,np.newaxis]
        formation_flying_distance = 10000
        formation_flying_strength = 0.125

        separations = self.positions[:,np.newaxis,:] - self.positions[:,:,np.newaxis]
        squared_displacements = separations * separations
        square_distances = np.sum(squared_displacements, 0)

        very_far=square_distances > formation_flying_distance
        velocity_separation_if_close = np.copy(velocity_separation)
        velocity_separation_if_close[0,:,:][very_far] =0
        velocity_separation_if_close[1,:,:][very_far] =0
        self.velocities -= np.mean(velocity_separation_if_close, 1) * formation_flying_strength
    
    def move_velocities(self):
        # Move according to velocities
        self.positions += self.velocities



class Animate_Boids(object):
    def __init__(self, positions, velocities):
        self.positions = positions
        self.velocities = velocities

    def animate(self, frame, scatter):
        update_boids(self.positions, self.velocities)
        scatter.set_offsets(zip(self.positions[0], self.positions[1]))

    def display(self):
        figure=plt.figure()
        axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
        scatter=axes.scatter(self.positions[0], self.positions[1])
        anim = animation.FuncAnimation(figure, self.animate, fargs=[scatter], frames=50, interval=50)
        plt.show()


def update_boids(positions, velocities):
    up_date = UpdateBoids(positions, velocities)
    up_date.to_middle()
    up_date.away_from()
    up_date.match_speed()
    up_date.move_velocities()


def parser():
    boids = NewBoids(50).return_boids()
    positions = boids[0]
    velocities = boids[1]

    Animate_Boids(positions, velocities).display()


if __name__ == "__main__":
    parser()
















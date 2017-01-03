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

boids=(positions[0], positions[1], velocities[0],velocities[1])



def update_boids(boids, positions, velocities):
    xs,ys,xvs,yvs=boids
    # Fly towards the middle
    strength_of_atraction = 0.01
    middle_of_flock = np.mean(positions, 1)
    direction_to_middle = positions - middle_of_flock[:, np.newaxis]
    velocities -= direction_to_middle*strength_of_atraction

    for i in range(Birds):
        for j in range(Birds):
            yvs[i]=yvs[i]+(ys[j]-ys[i])*0.01/len(xs)
    # Fly away from nearby boids
    for i in range(Birds):
        for j in range(Birds):
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 100:
                xvs[i]=xvs[i]+(xs[i]-xs[j])
                yvs[i]=yvs[i]+(ys[i]-ys[j])
    # Try to match speed with nearby boids
    for i in range(Birds):
        for j in range(Birds):
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 10000:
                xvs[i]=xvs[i]+(xvs[j]-xvs[i])*0.125/len(xs)
                yvs[i]=yvs[i]+(yvs[j]-yvs[i])*0.125/len(xs)
    # Move according to velocities
    positions += velocities


figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
    update_boids(boids, positions, velocities)
    scatter.set_offsets(zip(boids[0],boids[1]))

anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
















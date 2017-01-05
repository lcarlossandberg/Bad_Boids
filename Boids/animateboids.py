from matplotlib import pyplot as plt
from matplotlib import animation
from updateboids import UpdateBoids

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

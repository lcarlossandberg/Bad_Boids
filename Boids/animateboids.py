from matplotlib import pyplot as plt
from matplotlib import animation
from updateboids import UpdateBoids

class AnimateBoids(object):
    def __init__(self, positions, velocities, strength_of_atraction=0.01, alert_distance=100, formation_flying_distance=10000, formation_flying_strength=0.125):
        self.positions = positions
        self.velocities = velocities
    
        self.strength_of_atraction = strength_of_atraction
        self.alert_distance = alert_distance
        self.formation_flying_distance = formation_flying_distance
        self.formation_flying_strength = formation_flying_strength

    def update_boids(self, positions, velocities):
        up_date = UpdateBoids(positions, velocities, self.strength_of_atraction, self.alert_distance, self.formation_flying_distance, self.formation_flying_strength)
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

import numpy as np

class UpdateBoids(object):
    def __init__(self, positions, velocities, strength_of_atraction=0.01, alert_distance=100, formation_flying_distance=10000, formation_flying_strength=0.125):
        self.positions = positions
        self.velocities = velocities
        
        self.strength_of_atraction = strength_of_atraction
        self.alert_distance = alert_distance
        self.formation_flying_distance = formation_flying_distance
        self.formation_flying_strength = formation_flying_strength

    def to_middle(self):
        # Fly towards the middle
        #strength_of_atraction = 0.01
        middle_of_flock = np.mean(self.positions, 1)
        direction_to_middle = self.positions - middle_of_flock[:, np.newaxis]
        self.velocities -= direction_to_middle*self.strength_of_atraction

    def away_from(self):
        # Fly away from nearby boids
        separations = self.positions[:,np.newaxis,:] - self.positions[:,:,np.newaxis]
        squared_displacements = separations * separations
        square_distances = np.sum(squared_displacements, 0)
        #alert_distance = 100
        far_away = square_distances > self.alert_distance
        separations_if_close = np.copy(separations)
        separations_if_close[0,:,:][far_away] = 0
        separations_if_close[1,:,:][far_away] = 0
        self.velocities += np.sum(separations_if_close,1)


    def match_speed(self):
        # Try to match speed with nearby boids
        velocity_separation = self.velocities[:,np.newaxis,:] - self.velocities[:,:,np.newaxis]
        #formation_flying_distance = 10000
        #formation_flying_strength = 0.125

        separations = self.positions[:,np.newaxis,:] - self.positions[:,:,np.newaxis]
        squared_displacements = separations * separations
        square_distances = np.sum(squared_displacements, 0)

        very_far=square_distances > self.formation_flying_distance
        velocity_separation_if_close = np.copy(velocity_separation)
        velocity_separation_if_close[0,:,:][very_far] =0
        velocity_separation_if_close[1,:,:][very_far] =0
        self.velocities -= np.mean(velocity_separation_if_close, 1) * self.formation_flying_strength


    def move_velocities(self):
        # Move according to velocities
        self.positions += self.velocities


    def function_for_testing(self):
        #this function is used in testing to check the returns of the memeber functions
        return (self.positions, self.velocities)

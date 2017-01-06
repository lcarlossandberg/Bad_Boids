from nose.tools import assert_equal
import numpy as np
from matplotlib import pyplot as plt
from ..updateboids import UpdateBoids

"""
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
        
    def function_for_testing(self):
        #this function is used in testing to check the returns of the memeber functions
        return (self.positions, self.velocities)
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


ub = UpdateBoids(positions, velocities)

#velocities and positions for to_middle()
positions_to_middle = np.array([[0.57060007, 4.72023739, 9.2721358, 7.93680601, 4.28602204, 5.48081302,3.96498288, 1.73486068, 9.99097606, 1.96189901], [9.49748595, 4.9919118, 7.68153802, 4.31255511, 4.1212264,7.45132605, 0.33013738, 8.77902153, 3.30667064, 4.1014684 ]])

velocities_to_middle = np.array([[2.72485885, 0.97403056, 6.96403599, 2.17343107, 9.41927555, 2.02596887,6.36280911, 8.33661188, 4.91034246, 3.09335956], [ 1.58716287, 9.19986697, 4.60963656, 3.52968196,6.10808538, 2.29397324, 5.24123371, 1.0322892, 0.72209945, 8.20816059]])

def test_to_middle():
    ub.to_middle()
    (positions, velocities) = ub.function_for_testing()
    np.array_equal(positions, positions_to_middle)
    np.array_equal(velocities, velocities_to_middle)

test_to_middle()

#velocities and positions for away_from()
positions_away_from = np.array([[ 0.57060007, 4.72023739, 9.2721358, 7.93680601, 4.28602204, 5.48081302, 3.96498288, 1.73486068, 9.99097606, 1.96189901], [9.49748595, 4.9919118, 7.68153802, 4.31255511, 4.1212264,7.45132605, 0.33013738, 8.77902153, 3.30667064, 4.1014684 ]])

velocities_away_from = np.array([[-32.06809742, -1.7429285, 49.76606103, 31.62215821, 2.36016299, 6.91476611,-3.90669505, -24.23411428, 45.48039411, -27.2069833], [35.7978657, 4.54564361, 26.8516754, -7.9181083, -7.25299118, 22.23389238, -46.03073385, 34.24916314, -14.5937202, -5.35049677]])


def test_away_from():
    ub.away_from()
    (positions, velocities) = ub.function_for_testing()
    np.array_equal(positions, positions_away_from)
    np.array_equal(velocities, velocities_away_from)

test_away_from()


#velocities and positions for match_speed()
positions_match_speed = np.array([[0.57060007, 4.72023739, 9.2721358, 7.93680601, 4.28602204, 5.48081302,3.96498288, 1.73486068, 9.99097606, 1.96189901], [9.49748595, 4.9919118, 7.68153802, 4.31255511, 4.1212264,7.45132605, 0.33013738, 8.77902153, 3.30667064, 4.1014684 ]])

velocities_match_speed = np.array([[-27.47227619, -0.93775339, 44.13261245, 28.25669749, 2.65245167, 6.6377294,-2.83104912, -20.61754095, 40.3826539, -23.21880134], [31.85478486, 4.50909054, 24.02686835, -6.39669239,-5.81471491, 19.98630821, -39.74523975, 30.49967012, -12.2378528, -4.1500323 ]])


def test_match_speed():
    ub.match_speed()
    (positions, velocities) = ub.function_for_testing()
    np.array_equal(positions, positions_match_speed)
    np.array_equal(velocities, velocities_match_speed)

test_match_speed()


#velocities and positions for move_velocities()
positions_move_velocities = np.array([[-2.69016761e+01, 3.78248400e+00, 5.34047483e+01, 3.61935035e+01,6.93847371e+00, 1.21185424e+01, 1.13393376e+00, -1.88826803e+01, 5.03736300e+01, -2.12569023e+01], [4.13522708e+01, 9.50100234e+00, 3.17084064e+01, -2.08413728e+00, -1.69348843e+00, 2.74376343e+01,-3.94151024e+01, 3.92786916e+01, -8.93118216e+00, -4.85639019e-02]])

velocities_move_velocities = np.array([[-27.47227619, -0.93775339, 44.13261245, 28.25669749, 2.65245167,6.6377294, -2.83104912, -20.61754095, 40.3826539, -23.21880134], [31.85478486, 4.50909054, 24.02686835,-6.39669239, -5.81471491, 19.98630821, -39.74523975, 30.49967012, -12.2378528, -4.1500323]])

def test_move_velocities():
    ub.move_velocities()
    (positions, velocities) = ub.function_for_testing()
    np.array_equal(positions, positions_move_velocities)
    np.array_equal(velocities, velocities_move_velocities)

test_move_velocities()




import argparse
from newboids import NewBoids
from animateboids import AnimateBoids



def parser():
    parser = argparse.ArgumentParser(description = 'This is a simulation of boids')
    parser.add_argument('--count', type=int, default='50', required=False, help='The number of boids in the simulation')
    parser.add_argument('--attraction', type=float, default='0.01', required=False, help='The strenght of the attraction between the boids')
    parser.add_argument('--alert', type=float, default='100', required=False, help='The distance at which the boids avoid each other')
    parser.add_argument('--formation', type=float, default='10000', required=False, help='The distance at which the boids try to match each others speed')
    parser.add_argument('--strength', type=float, default='0.125', required=False, help='The strength with which the boids try to come together')
    
    args=parser.parse_args()


    
    
    boids = NewBoids(args.count).return_boids()
    positions = boids[0]
    velocities = boids[1]

    AnimateBoids(positions, velocities, args.attraction, args.alert, args.formation, args.strength).display()


if __name__ == "__main__":
    parser()

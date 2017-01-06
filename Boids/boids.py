import argparse
import yaml
from StringIO import StringIO
from newboids import NewBoids
from animateboids import AnimateBoids



def parser():
    parser = argparse.ArgumentParser(description = 'This is a simulation of boids')
    parser.add_argument('--argfile', type=str, required=False, help='This is used to select a file to be used to input the arguments, this file should have a dictionary in it')
    parser.add_argument('--count', type=int, default='50', required=False, help='The number of boids in the simulation')
    parser.add_argument('--attraction', type=float, default='0.01', required=False, help='The strenght of the attraction between the boids')
    parser.add_argument('--alert', type=float, default='100', required=False, help='The distance at which the boids avoid each other')
    parser.add_argument('--formation', type=float, default='10000', required=False, help='The distance at which the boids try to match each others speed')
    parser.add_argument('--strength', type=float, default='0.125', required=False, help='The strength with which the boids try to come together')
    parser.add_argument('--save', type=bool, default=False, required=False, help='Do you want to save the animation to a file, either True or False, must have relevent drivers installed to do this')
    parser.add_argument('--name', type=str, default='boids_1.mp4', required=False, help='If saving to a file the name of the file you wish to save it to')
    
    args=parser.parse_args()



    if args.argfile:
        file_args = {}
        open_file = open(args.argfile, 'r')
        file_args = yaml.load(open_file)
        open_file.close()


        boids = NewBoids(file_args['count']).return_boids()
        positions = boids[0]
        velocities = boids[1]

        AnimateBoids(positions, velocities, file_args['attraction'], file_args['alert'], file_args['formation'], file_args['strength'], (file_args['save'], file_args['name'])).display()
    else:
        
        boids = NewBoids(args.count).return_boids()
        positions = boids[0]
        velocities = boids[1]

        AnimateBoids(positions, velocities, args.attraction, args.alert, args.formation, args.strength, (args.save, args.name)).display()


if __name__ == "__main__":
    parser()

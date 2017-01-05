from newboids import NewBoids
from animateboids import AnimateBoids


def parser():
    boids = NewBoids(50).return_boids()
    positions = boids[0]
    velocities = boids[1]

    AnimateBoids(positions, velocities).display()


if __name__ == "__main__":
    parser()

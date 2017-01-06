from setuptools import setup, find_packages

setup(
      name = "boid",
      version = "2.7.13",
      packages = find_packages(exclude=['*test']),
      scripts = ['scripts/boids'],
      
      install_requires = ['argparse','numpy','StringIO', 'matplotlib']
      
)

from setuptools import setup, find_packages

setup(
      name = "Boids",
      version = "6.6.2",
      description = "Simulation of Boids",
      author = "Leo Carlos-Sandberg"
      url = "https://github.com/lcarlossandberg/Bad_Boids",
      license = "MIT License"
      packages = find_packages(exclude=['*test']),
      scripts = ['scripts/Boids'],
      
      install_requires = ['argparse','numpy', 'matplotlib']
      
)

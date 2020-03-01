"""
lj.py
A python package to perfom Markov chain Monte Carlo simulation of Lennard Jones (12-6) fluid particles in canonical (NVT) ensemble.

Handles the primary functions
"""

# import libraries

import os
import math
import random
from atom import Atom

class Simulation:

    """
        Parameters and constants
    """

    kB = 1                      # Boltzmann constant
    N = 500                     # Number of atoms
    sigma = 1
    epsilon = 1
    mass = 1
    rcut = 2.5
    steps = 100000
    temp    = 8.5e-1
    density = 1.0e-3
    L =  (N/density)**(1.0/3.0)
    atoms = []

    def __init__(self):

        """
            Creates a simulation with N atoms
        """

        print("Initializing system...")

        for i in range(0,self.N):
            self.atoms.append(Atom())

        # set the epsilon, sigma, and mass parameters
        for index in range(0,N):
            self.atoms[index].sigma = sigma
            self.atoms[index].eps = epsilon
            self.atoms[index].mass = mass

        self.assignPosition();    


    def assignPositions(self):

        """
            Initialize the simulation Box
            Place all the atoms randomly in the box
        """

        for index in range(0, N):
            self.atom[index].x = random.uniform(0, L)
            self.atom[index].y = random.uniform(0, L)
            self.atom[index].z = random.uniform(0, L)


    def perodicBoundaryCondition(atom):

        """
            Apply perodic boundary conditions.
        """

        if atom.x > L:
            atom.x -= L
        elif atom.x < 0:
            atom.x += L
        if atom.y > L:
            atom.y -= L
        elif atom.y < 0:
            atom.y += L
        if atom.z > L:
            atom.z -= L
        elif atom.z < 0:
            atom.z += L  

        return atom

    def writeEnergy(step, energy):

	'''
		Writes the energy to a file.
	'''
	
		with open('energy.dat', 'a') as f:
			f.write('{0} {1}\n'.format(step, energy))


    def runSimulation(self):
        """



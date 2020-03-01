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
import energy

class Simulation:

    """
        Parameters and constants
    """

    kB = 1                      # Boltzmann constant
    N = 500                     # Number of atoms
    sigma = 1					# Size parameter
    epsilon = 1					# Energy parameter
    mass = 1					# mass of atoms
    rcut = 2.5					# cut-off distance
    nsteps = 100000				# Total number of MC steps
    temp    = 8.5e-1			# Temperature
    density = 1.0e-3			# density
    L =  (N/density)**(1.0/3.0) # Box length
    atoms = []					# Array to store atoms

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

        self.assignPosition()
        energy = self.updateEnergy()

        if os.path.exists('energy.dat'):
			os.remove('energy.dat')

		writeEnergy(str(0), str(energy))

        print("done.")   


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


	def updateEnergy(self):

		"""
			Calculates the net potential on each atom, applying a cutoff radius
		"""

		energy = 0

		for atom1 in range(0, self.N-1):
            for atom2 in range(atom1+1, self.N):
            	energy += energy(atom1, atom2, rcut)

        return energy


    def runSimulation(self):

        """
        	Runs Monte Carlo simulations for number of nsteps.
        """







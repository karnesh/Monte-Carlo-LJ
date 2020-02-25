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

    kB = 1
    N = 500
    sigma = 1
    epsilon = 1
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


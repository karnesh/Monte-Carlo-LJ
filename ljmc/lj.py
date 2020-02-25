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

def perodicBoundaryCondition(self):
    '''Apply perodic boundary conditions.'''
    if self.atom.x > L:
        self.atom.x -= L
    elif self.atom.x < 0:
        self.atom.x += L
    if self.atom.y > L:
        self.atom.y -= L
    elif self.atom.y < 0:
        self.atom.y += L
    if self.atom.z > L:
        self.atom.z -= L
    elif self.atom.z < 0:
        self.atom.z += L  


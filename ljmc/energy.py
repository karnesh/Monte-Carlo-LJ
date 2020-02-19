"""
energy.py

function that computes the inter particle energy
It uses truncated 12-6 Lennard Jones potential
All the variables are in reduced units.

"""

# Import libraries
import math

def energy(atom1, atom2, rc):
    '''calculates the energy of the system'''

    eps = atom1.eps
    sig = atom1.sigma
    rcsq = rc**2
    





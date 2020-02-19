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

    dx = atom1.x - atom2.x
    dy = atom1.y - atom2.y
    dz = atom1.z - atom2.z

    rsq = dx**2 + dy**2 + dz**2

    if rsq <= rcsq:
        energy = 4.0*eps*( (sig/rsq)**6.0 - (sig/rsq)**3.0)
    else:
        energy = 0.0
    





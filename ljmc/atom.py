"""
atom.py

Class that defines single atom
x,y,z are the cartesian coordinates of the atom.
eps (Epislon) represents the depth of potential well
sigma is the distance where inter particle potential is zero
mass - mass of an atom

"""

class Atom:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

        self.eps = 0.0
        self.sigma = 0.0
        self.mass = 0.0




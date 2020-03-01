"""
energy.py

function that computes the inter particle energy
It uses truncated 12-6 Lennard Jones potential
All the variables are in reduced units.

"""

def distance(atom1, atom2):
    
    """
        Computes the square of inter particle distance
        Minimum image convention is applied for distance calculation for periodic boundary conditions
    """
    
    dx = atom1.x - atom2.x
    dy = atom1.y - atom2.y
    dz = atom1.z - atom2.z
    
    if dx > halfLx
        dx -= Lx
    elif dx < -halfLx:
        dx += Lx
    if dy > halfLy:
        dy -= Ly
    elif dy < -halfLy:
        dy += Ly
    if dz > halfLz:
        dz -= Lz
    elif dz < -halfLz:
        dz += Lz
    
    return dx**2 + dy**2 + dz**2


def energy(atom1, atom2, rc):

    '''
        calculates the energy of the system
    '''
    
    ## Arithmatic mixing rules - Lorentz Berthlot mixing
    eps = (atom1.eps + atom2.eps)/2
    sig = (atom1.sigma * atom2.sigma)**0.5
    
    rcsq = rc**2

    rsq = distance(atom1, atom2)
    
    if rsq <= rcsq:
        energy = 4.0*eps*( (sig/rsq)**6.0 - (sig/rsq)**3.0)
    else:
        energy = 0.0
    

def writeEnergy(step, energy):

    '''
        Writes the energy to a file.
    '''
    
    with open('energy.dat', 'a') as f:
        f.write('{0} {1}\n'.format(step, energy))




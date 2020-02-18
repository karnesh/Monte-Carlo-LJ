"""
LennardJonesMC
A python package to perfom Markov chain Monte Carlo simulation of Lennard Jones (12-6) fluid particles in canonical (NVT) ensemble.
"""

# Add imports here
from .lj import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions

import argparse
import sys
import math
import numpy as np

#-------------------------------------------
# Create the parser
parser = argparse.ArgumentParser(description=script_description,formatter_class=argparse.RawDescriptionHelpFormatter)
# Define the command-line arguments
parser.add_argument('-p', '--prefix', default='SYSTEM', help="Prefix for topology, restraints and trajectory files.")
parser.add_argument('-d', '--dihelist', default='dihe.list', help="Dihedrals definition file.")
parser.add_argument('-k', '--forceconstant',  default=100, help="Force constant (kcal mol-1 degree-2)")

# If no arguments are provided, print the description and exit
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit()

# Parse the arguments
args = parser.parse_args()

# Assign values from args
prefix = args.prefix
dihelist = args.dihelist
forceconstant = args.forceconstant

# The main code starts here <------------------------------------------------------------------

# Reads data
dihelist=np.loadtxt(dihelist_name,dtype='int')


ndihe = len(dihelist)



dihetraj = np.empty((nsteps,ndihe))
print("\n Calculating dihedrals temporal traces...\n")

for i in range(0,ndihe):
    print(" --> Dihedral", i+1, "( out of ",ndihe,")")
    dihetraj[:,i]=calculate_dihedral(coordinates,dihelist[i][0],dihelist[i][1],dihelist[i][2],dihelist[i][3])
print("\n These results will be saved to 'dihetraj.dat' file...\n")
fmt = ['%d'] + ['%.4f'] * ndihe
indices=np.arange(nsteps)
np.savetxt('dihetraj.dat',np.column_stack((indices,dihetraj)),fmt=fmt)


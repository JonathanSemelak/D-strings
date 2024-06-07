import argparse
import sys
import math
import numpy as np


# def print_welcome_message(script_description):
#     print(script_description)

# def check_bool(inputvariable,rightvariable):
#     if inputvariable not in ['True','False']:
#         sys.exit("Error: "+ rightvariable + " must be 'True' or 'False'")

# #-------------------------------------------
# # Create the parser
# parser = argparse.ArgumentParser(description=script_description,formatter_class=argparse.RawDescriptionHelpFormatter)
# # Define the command-line arguments
# parser.add_argument('-i', '--input', required=True, help='Input file name')
# parser.add_argument('-d', '--dihelist', default='none', help="A text file with the atom index of each dihedral to be extracted (not needed if format is 'dihe')")
# parser.add_argument('-f', '--format', required=True, help="Input file format ('xyz', 'netcdf'  or 'dihe')")
# parser.add_argument('-id', '--id', default=0, help="Intrinsic dimension")
# parser.add_argument('-v', '--visualize', default="False", help="Intrinsic dimension")
# parser.add_argument('-ha', '--halo', default="False", help="Use halo for ADP")
# parser.add_argument('-z', '--zvalue',  default=3.5, help="Z value for ADP")
# parser.add_argument('-wt', '--writetrajs', default="False", help="Write a trajectory file for each cluster")
# parser.add_argument('-wf', '--writefreq', default=1, help="Writting frequence (for --writetrajs/-wt option)")
# parser.add_argument('-nj', '--njobs', default=1, help="Number of threads for ADP calculation")
# parser.add_argument('-s', '--slice', nargs=2, type=int, default=[0, 0], help='Analize a slice of the data (frame count starts with zero)')
# parser.add_argument('-rc', '--randomchoice', default=0, type=int, help="Makes a random choice of --randomchoice/-rc frames")

# # If no arguments are provided, print the description and exit
# if len(sys.argv) == 1:
#     parser.print_help()
#     sys.exit()

# # Parse the arguments
# args = parser.parse_args()

# # Assign values from args
# input_name = args.input
# dihelist_name = args.dihelist
# file_format = args.format
# z_value = args.zvalue
# freq_write = int(args.writefreq)

# # Checks the variables are str True or False before converting to bool
# check_bool(args.visualize,"--visualize ( -v)")
# visualize = args.visualize == "True"

# check_bool(args.halo,"--halo ( -ha)")
# halo = args.halo == "True"

# check_bool(args.writetrajs,"--writetrajs ( -wt)")
# write_trajs = args.writetrajs == "True"

# Call the function at the beginning of your main script execution
if __name__ == "__main__":
    print_welcome_message(script_description)
    # Rest of your script follows here...

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


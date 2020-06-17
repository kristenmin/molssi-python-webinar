"""
this module has functions associated wit hanalyzing the geometry of a molecule.
"""

# open as txt, copy and paste the code from the notebook, and then name py to have it recognize the python code!

# to run in terminal, python geometry-analysis.py data/water.xyz

import numpy
import os
import argparse #user input = argument

def calculate_distance(coords1, coords2): #calculate_distance is a function that's modular - can be used anywhere
    x_distance = coords1[0] - coords2[0]
    y_distance = coords1[1] - coords2[1]
    z_distance = coords1[2] - coords2[2]
    distance_12 = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return distance_12

def bond_check(atom_distance, min_length = 0, max_length = 1.5):
    """
    check if a distance is a bond based on a minimum and maximum length. 
    inputs: distance, min_length, max_length
    defaults: min_length = 0, max_length = 1.5
    return: true or false
    """
    if atom_distance > min_length and atom_distance <= max_length:
        return True
    else: 
        return False

# opens and processes xyz file -- takes an xyz file as a parameter and returns the symbols and coordinates. 
def open_xyz(filename):
    xyz_file = numpy.genfromtxt(fname = filename, skip_header = 2, dtype = 'unicode')
    symbols = xyz_file[:, 0]
    coord = (xyz_file[:, 1:])
    coord = coord.astype(numpy.float)
    return symbols, coord

#EVERYTHING BELOW: MAIN PART OF THE CODE 
if __name__ == "__main__": #syntax telling python that it is the main code

    #create parser object  
    parser = argparse.ArgumentParser(description = "this script analyzes a user provided xyz file and outputs all the bonds.") 
    parser.add_argument("xyz_file", help = "the filepath for the xyz file to analyze") #name and the help message
    args = parser.parse_args() #argparse is doing the work and collect the argument from the user

    file_location = args.xyz_file #instead of os.path.join
    xyz_file = numpy.genfromtxt(fname = file_location, skip_header = 2, dtype = 'unicode')
    symbols = xyz_file[:, 0]
    coordinates = xyz_file[:, 1:]
    coordinates = coordinates.astype(numpy.float)
    num_atoms = len(symbols)
    for num1 in range(0, num_atoms): 
        for num2 in range(0, num_atoms):
            if num1 < num2:
                distance = calculate_distance(coordinates[num1], coordinates[num2])
                if bond_check(distance) is True: # use bond_check
                    print(F'{symbols[num1]} to {symbols[num2]} : {distance:.3f}')
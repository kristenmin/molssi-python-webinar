# answer to homework 3

import os
import argparse

# tell argparse to handle arguments
parser = argparse.ArgumentParser(description = "this script parses amber mdout files to extract the total energy.")

# tell argparse what arguments to expect
parser.add_argument("path", help = "the filepath to the file to ne analyzed.")

# get arguments from the user
args = parser.parse_args()

# Open the file for reading
filename = args.path #os.path.join not needed
f = open(filename, 'r')

# Read the data in the file. 
data = f.readlines()
f.close()

# Open a file for writing
base_filename = filename.split('.')
base_filename = base_filename[0]
output_filename = F'{base_filename}_Etot.txt'

f_write = open(output_filename, 'w+')

print(F'Writing output to {output_filename}')

f_write.write('total energy\n')

# Loop through lines in the file. 
etot = []

for line in data: 
    split_line = line.split()
    
    # Get information from the line. 
    if 'Etot' in line:
        etot.append(split_line[2])

# overwrite the original list
etot = etot[:-2] # get everything but the last two

for energy in etot:
    f_write.write(F"{energy}\n")

# write information to new file. 
f_write.close()
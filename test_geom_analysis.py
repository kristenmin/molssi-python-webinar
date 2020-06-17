# Testing code with pytest

# writing unit tests
import geom_analysis as ga # the file must be in the same directory as our test file. 

def test_calculate_distance():
    coord1 = [0, 0, 0]
    coord2 = [1, 0, 0]
    expected = 1.0
    observed = ga.calculate_distance(coord1, coord2)
    assert observed == expected # states what should be true in our test. 
    
def test_bond_check():
    bond_distance = 1.2
    expected = True
    observed = ga.bond_check(bond_distance)
    assert observed == expected   
# to run the test in command line, pytest. 


# edge cases and corner cases

def test_bond_check_true():
    bond_distance = 1.2
    expected = True
    observed = ga.bond_check(bond_distance)
    assert observed == expected
    
def test_bond_check_false():
    bond_distance = 2.0
    expected = False
    observed = ga.bond_check(bond_distance)
    assert observed == expected

def test_bond_check_0():
    bond_distance = 0
    expected = False
    observed = ga.bond_check(bond_distance)
    assert observed == expected
    
def test_bond_check_1_5():
    bond_distance = 1.5
    expected = True
    observed = ga.bond_check(bond_distance)
    assert observed == expected


# raising errors

# syntax 
    # raise ErrorType("your error message here")

# value error = "raised when an operation or function receives an argument that has the right type but an inapproiate value"
def bond_check(atom_distance, minimum_length=0, maximum_length=1.5):
    if atom_distance < 0: # ValueError if negative value
        raise ValueError(F'Invalid atom distance {atom_distance}. Distance can not be less than 0!') 
    if atom_distance > minimum_length and atom_distance <= maximum_length:
        return True
    else:
        return False

# test that this error is raised
def test_bond_check_negative():
    distance = -1
    expected = False
    calculated = ga.bond_check(distance)
    assert expected == calculated

# make sure the corror error is raised.
import pytest

def test_bond_check_negative():
    distance = -1
    expected = False
    with pytest.raises(ValueError)
        calculated = ga.bond_check(distance)

# example -- write an exception into open_xyz function. raise a ValueError if the file extension is not .xyz.
def open_xyz(filename):
    fpath, extension = os.path.splitext(filename)

    if extension.lower() != '.xyz':
        raise ValueError("Incorrect file type! File must be type xyz")

    xyz_file = numpy.genfromtxt(fname=filename, skip_header=2, dtype='unicode')
    symbols = xyz_file[:,0]
    coord = (xyz_file[:,1:])
    coord = coord.astype(numpy.float)
    return symbols, coord

with pytest.raises(ValueError):
    ga.open_xyz(fname)
#import to allow for named tuples
from collections import namedtuple

#create a constant for comparison later on
CLOSEENOUGH = 0.00001

#Create a new class using namedtuple with the name Tuples and then specify its attributes
Tuples = namedtuple('TuplePoint',['x' , 'y' , 'z' , 'w'])

#Create a way to tell if a tuple is a point or a vector
def IsPoint(x,y,z,w):
	return (w > CLOSEENOUGH)

def IsVector(x,y,z,w):
	return (w < CLOSEENOUGH)

#create a way to create vectors or points fast

def PointTuple(x,y,z):
	return Tuples(x, y, z, 1.0)

def VectorTuple(x,y,z):
	return Tuples(x, y, z, 0)

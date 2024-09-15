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

#create operations for your tuples
def AddingTuple(x1,y1,z1,w1 , x2,y2,z2,w2):
	return (x1+x2,y1+y2,z1+z2,w1+w2)

def SubtractTuple(x1,y1,z1,w1 , x2,y2,z2,w2):
	return (x1-x2,y1-y2,z1-z2,w1-w2)

#create a function to check for equality among tuples
def IsTupleEqual(x1,y1,z1,w1 , x2,y2,z2,w2):
	return ((x1,y1,z1,w1) == (x2,y2,z2,w2))
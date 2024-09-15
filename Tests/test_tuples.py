import unittest
import tuples

#create a class name it whatever you want but make sure it inherits unittest.TestCase 
class TestTuples(unittest.TestCase):
#have to start function with test_ or it wont run and just have your test cases	
	def test_isPoint(self):
		result = tuples.IsPoint(4.3, -4.2, 3.1, 0.89)
		self.assertTrue(result)

	def test_isVector(self):
		result = tuples.IsVector(4.3, -4.2, 3.1, 0)
		self.assertTrue(result)

	def test_Point(self):
		PointTest = tuples.PointTuple(4.3, -4.2, 3.1)
		self.assertEqual(PointTest.w, 1.0)

	def test_Vector(self):
		VectorTest = tuples.VectorTuple(4.3, -4.2, 3.1)
		self.assertEqual(VectorTest.w, 0)

	def test_addTuples(self):
		AddTest = tuples.AddingTuple(3,-2,5,1 , -2,3,1,0)
		self.assertEqual(AddTest ,(1,1,6,1))

	def test_subTuples(self):
		SubTest = tuples.SubtractTuple(3,2,1,0,  5,6,7,0)
		self.assertEqual(SubTest , (-2,-4,-6,0))

	def test_equalTuples(self):
		result = tuples.IsTupleEqual(1,1,1,1, 1,1,1,1)
		self.assertTrue(result)
#this is just used to run the test directly inside text editor
if __name__ == '__main__':
	unittest.main()


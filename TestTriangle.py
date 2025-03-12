# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestRightTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(4,5,3),'Right','4,5,3 is a Right triangle')

class TestEquilateralTriangles(unittest.TestCase):
        
    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTriangleB(self): 
        self.assertEqual(classifyTriangle(15,15,15),'Equilateral','15,15,15 should be equilateral')

    def testEquilateralTriangleC(self): 
        self.assertEqual(classifyTriangle(50,50,50),'Equilateral','50,50,50 should be equilateral')

class TestScaleneTriangles(unittest.TestCase):

    def testScaleneTriangleA(self): 
        self.assertEqual(classifyTriangle(1,2,3),'Scalene','1,2,3 should be scalene')

    def testScaleneTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,7),'Scalene','5,3,7 should be scalene')

    def testScaleneTriangleC(self): 
        self.assertEqual(classifyTriangle(8,9,2),'Scalene','8,9,2 should be scalene')

class TestIsocelesTriangles(unittest.TestCase):

    def testIsocelesTriangleA(self): 
        self.assertEqual(classifyTriangle(3,3,5),'Isoceles','3,3,5 should be isoceles')

    def testIsocelesTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,5),'Isoceles','5,3,5 should be isoceles')

    def testIsocelesTriangleC(self): 
        self.assertEqual(classifyTriangle(8,2,2),'Isoceles','8,2,2 should be isoceles')

class TestInvalidInputs(unittest.TestCase):

    def testInvalidInputA1(self):
        self.assertEqual(classifyTriangle(250,15,15), 'InvalidInput', '250,15,15 should be InvalidInput')

    def testInvalidInputA2(self):
        self.assertEqual(classifyTriangle(15,215,15), 'InvalidInput', '15,215,15 should be InvalidInput')

    def testInvalidInputA3(self):
        self.assertEqual(classifyTriangle(5,20,201), 'InvalidInput', '5,20,201 should be InvalidInput')

    def testInvalidInputB1(self):
        self.assertEqual(classifyTriangle(15,20,-3), 'InvalidInput', '15,20,-3 should be InvalidInput')

    def testInvalidInputB2(self):
        self.assertEqual(classifyTriangle(15,-20,30), 'InvalidInput', '15,-20,30 should be InvalidInput')

    def testInvalidInputB3(self):
        self.assertEqual(classifyTriangle(0,20,19), 'InvalidInput', '0,20,19 should be InvalidInput')

    def testInvalidInputC1(self):
        self.assertEqual(classifyTriangle(True,20,19), 'InvalidInput', 'True,20,19 should be InvalidInput')

    def testInvalidInputC2(self):
        self.assertEqual(classifyTriangle(80,False,19), 'InvalidInput', '80,False,19 should be InvalidInput') 

    def testInvalidInputC3(self):
        self.assertEqual(classifyTriangle(5,4,8.8), 'InvalidInput', '5,4,8.8 should be InvalidInput')       


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()


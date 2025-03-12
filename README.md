# Homework 6b: Testing a Legacy Systems
The objective of this assignment is for you to
1.  develop a set of test-cases for an existing triangle classification program,
2.  use those test-cases to find and fix defects in that program, and
3.  report on your testing results for the Triangle problem

Sometimes you will be given a program that someone else has written, and you will be asked to fix, update and enhance that program.   In this assignment you will start with an existing implementation of the classify triangle program that will be given to you.   You will also be given a starter test program that tests the classify triangle program, but those tests are not complete.  

These are the two files:  `Triangle.py` and `TestTriangle.py`
1. `Triangle.py` is a starter implementation of the triangle classification program.
2. `TestTriangle.py` contains a starter set of unittest test cases to test the classifyTriangle() function in the file Triangle.py file.   

In order to determine if the program is correctly implemented, you will need to update the set of test cases in the test program.  You will need to update the test program until you feel that your tests adequately test all of the conditions.   Then you should run the complete set of tests against the original triangle program to see how correct the triangle program is.    Capture and then report on those results in a formal test report described below.   For this first part you should not make any changes to the classify triangle program.  You should only change the test program.

Based on the results of your initial tests, you will then update the classify triangle program to fix all defects.  Continue to run the test cases as you fix defects until all of the defects have been fixed.   Run one final execution of the test program and capture and then report on those results in a formal test report described below.   

Note that you should NOT simply replace the logic with your logic from Assignment 1.  Test teams typically don't have the luxury of rewriting code from scratch and instead must fix what's delivered to the test team.   

---

**Author:** Carson Lee

**Pledge:** *I pledge my honor that I have abided by the Stevens Honor System.*

## Summary


## Detailed Results
### Part 0


### Part 1
Running coverage on `TestTriangle.py` reveals just how much we're missing
```
Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
TestTriangle.py      14      1    93%   24
Triangle.py          16     12    25%   32, 39-57
-----------------------------------------------
TOTAL                30     13    57%
```

Enhanced set of test cases for the `classifyTriangle()` function on the orginal `Triangle.py` code.
| **Test ID**              | **Input**  | **Expected Results** | **Actual Result** | **Pass or Fail** |
| ------------------------ | :--------: | :------------------: | :---------------: | :--------------: |
| testRightTriangleA       | (3,4,5)    | Right                | InvalidInput      | Fail             |
| testRightTriangleB       | (5,3,4)    | Right                | InvalidInput      | Fail             |
| testRightTriangleC       | (4,5,3)    | Right                | InvalidInput      | Fail             |
| testEquilateralTriangleA | (1,1,1)    | Equilateral          | InvalidInput      | Fail             |
| testEquilateralTriangleB | (15,15,15) | Equilateral          | InvalidInput      | Fail             |
| testEquilateralTriangleC | (50,50,50) | Equilateral          | InvalidInput      | Fail             |
| testScaleneTriangleA     | (1,2,3)    | Scalene              | InvalidInput      | Fail             |
| testScaleneTriangleB     | (5,3,7)    | Scalene              | InvalidInput      | Fail             |
| testScaleneTriangleC     | (8,9,2)    | Scalene              | InvalidInput      | Fail             |
| testIsocelesTriangleA    | (3,3,5)    | Isoceles             | InvalidInput      | Fail             |
| testIsocelesTriangleB    | (5,3,5)    | Isoceles             | InvalidInput      | Fail             |
| testIsocelesTriangleC    | (8,2,2)    | Isoceles             | InvalidInput      | Fail             |

### Part 2
Same set of test cases from Part 1, but now tested on the modified `Triangle.py` code.

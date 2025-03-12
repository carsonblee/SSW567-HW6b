# Homework 6b: Testing a Legacy Systems
[![CircleCI](https://dl.circleci.com/status-badge/img/circleci/YBMEBAqhQKNrvTPDbdRbap/Q57JhqGVTKYXoQE4s7Yvuy/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/circleci/YBMEBAqhQKNrvTPDbdRbap/Q57JhqGVTKYXoQE4s7Yvuy/tree/main)
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
Working on this assignment, I started with one set of tests that had a total of 12 test cases. The test cases were designed so that each triangle type would be classified and tested 3 times with each time the inputs being in a different order to replicate the different size and arrangements of triangles. After the first run resulting in all failures, I knew something was getting caught in the `Triangle.py` code. After fixing that bug, I ran the code again and saw 5 issues arise, some for each type of triangle classification. Fixing those resulted in all 12 test cases passing, but it didn't feel like enough. Code coverage showed that my test cases haven't even touched some parts of the `Triangle.py` code - that's an issue.

This resulted in the additon of 9 more test cases to the test set, this time to address the InvalidInput returns and make sure the code didn't process invalid inputs as triangles. Running this resulted in one failure since the code was accepting a boolean and treating it like a valid triangle side. Once that was fixed, there were no more failures in the test cases and code coverage was at 100%.

This assignment has really helped me understand the thoroughness that comes with testing legacy code. While I knew it would be similar to writing tests for code I wrote, I also realized that in some ways it would be different. For example, after writing some simple tests and trying them out for the first time, I noticed that they all failed unexpectedly since they all returned InvalidInput. I then had to go through the source code and really understand what was happening before I even started modifying the code. While it was easy to do in this case, I understand that's not always the case and things become a lot hard when there's more lines of code and more complex code in place, so I really did understand the point of the assignment. I personally thought that this was a good way to introduce testing in legacy systems. I could see more complex assignments later on being something like developing test cases for a blackbox system where you can't see the code. The one annoying thing about this assignment was the level of documentation I felt I needed to provide for the end results. While it can be useful, I felt like it was bit excessive.

## Detailed Results
The following information lists the detailed results for this assignment when it came to developing test cases, what inputs were given, and the thought process behind everything.

### Part 1: New Test Cases
I started with running a code coverage on `TestTriangle.py` to see just how much we're missing.
```bash
$   coverage run TestTriangle.py
$   coverage report -m
```

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
| :----------------------- | :--------: | :------------------ | :--------------- | :--------------: |
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

Obviously, not a great first run at these test cases. I wanted to include three test cases for each type of triangle that can be classified. One important part of designing these tests was to move the numbers around so the numbers weren't always inputted in ascending order. Despite having three test cases for each type of triangle, I had a feeling that these test cases were all getting caught up on the same line of buggy code. An output of the test run can be found in the [test run 1 output file](./Output%20Files/TestRun1.txt).

### Part 2: Modified Code
Now working with the same set of test cases from Part 1, but now on the modified `Triangle.py` code.
| **Test ID**              | **Input**  | **Expected Results** | **Actual Result** | **Pass or Fail** |
| :----------------------- | :--------: | :------------------ | :--------------- | :--------------: |
| testRightTriangleA       | (3,4,5)    | Right                | Right             | Pass             |
| testRightTriangleB       | (5,3,4)    | Right                | Right             | Pass             |
| testRightTriangleC       | (4,5,3)    | Right                | Right             | Pass             |
| testEquilateralTriangleA | (1,1,1)    | Equilateral          | Equilateral       | Pass             |
| testEquilateralTriangleB | (15,15,15) | Equilateral          | Equilateral       | Pass             |
| testEquilateralTriangleC | (50,50,50) | Equilateral          | Equilateral       | Pass             |
| testScaleneTriangleA     | (1,2,3)    | Scalene              | Scalene           | Pass             |
| testScaleneTriangleB     | (5,3,7)    | Scalene              | Scalene           | Pass             |
| testScaleneTriangleC     | (8,9,2)    | Scalene              | Scalene           | Pass             |
| testIsocelesTriangleA    | (3,3,5)    | Isoceles             | Isoceles          | Pass             |
| testIsocelesTriangleB    | (5,3,5)    | Isoceles             | Isoceles          | Pass             |
| testIsocelesTriangleC    | (8,2,2)    | Isoceles             | Isoceles          | Pass             |

While the result of these test cases is looking a lot better, there is still a more we can do to ensure all parts of the code are working and covered. The results of running these test cases can be found in the [test run 2 output file](./Output%20Files/TestRun2.txt) where it shows that all twelve of the test cases have passed flawlessly. 

Running code coverage again reveals that there are still some missing peices of code that aren't covered by the current test cases. While all the triangle cases are covered, we have not accounted for the InvalidInput cases - a key part of the code.
```
Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
TestTriangle.py      33      0   100%
Triangle.py          14      3    79%   32, 35, 40
-----------------------------------------------
TOTAL                47      3    94%
```

### Part 3: More Test Cases
Working off of the code coverage report, it's obvious we need test cases for the InvalidInputs code that catch those invalid inputs in the beginning of the `classifyTriangle()` function. Adding these tests gives us a more robust set of tests resulting in better source code.

Now including the new test cases that account for invalid inputs and run on the modified `Triangle.py` code, we get the following [output for test run 3](./Output%20Files/TestRun3.txt):
| **Test ID**              | **Input**         | **Expected Results** | **Actual Result** | **Pass or Fail** |
| :----------------------- | :---------------: | :---------------- | :------------- | :------------: |
| testRightTriangleA       | (3,4,5)           | Right            | Right         | Pass         |
| testRightTriangleB       | (5,3,4)           | Right            | Right         | Pass         |
| testRightTriangleC       | (4,5,3)           | Right            | Right         | Pass         |
| testEquilateralTriangleA | (1,1,1)           | Equilateral      | Equilateral   | Pass         |
| testEquilateralTriangleB | (15,15,15)        | Equilateral      | Equilateral   | Pass         |
| testEquilateralTriangleC | (50,50,50)        | Equilateral      | Equilateral   | Pass         |
| testScaleneTriangleA     | (1,2,3)           | Scalene          | Scalene       | Pass         |
| testScaleneTriangleB     | (5,3,7)           | Scalene          | Scalene       | Pass         |
| testScaleneTriangleC     | (8,9,2)           | Scalene          | Scalene       | Pass         |
| testIsocelesTriangleA    | (3,3,5)           | Isoceles         | Isoceles      | Pass         |
| testIsocelesTriangleB    | (5,3,5)           | Isoceles         | Isoceles      | Pass         |
| testIsocelesTriangleC    | (8,2,2)           | Isoceles         | Isoceles      | Pass         |
| testInvalidInputA1       | (250,15,15)       | InvalidInput     | InvalidInput  | Pass         |
| testInvalidInputA2       | (15,215,15)       | InvalidInput     | InvalidInput  | Pass         |
| testInvalidInputA3       | (5,20,201)        | InvalidInput     | InvalidInput  | Pass         |
| testInvalidInputB1       | (15,20,-3)        | InvalidInput     | InvalidInput  | Pass         |
| testInvalidInputB2       | (15,-20,30)       | InvalidInput     | InvalidInput  | Pass         |
| testInvalidInputB3       | (0,20,19)         | InvalidInput     | InvalidInput  | Pass         |
| testInvalidInputC1       | (True,20,19)      | InvalidInput     | Scalene       | Fail         |
| testInvalidInputC2       | (80,False,19)     | InvalidInput     | InvalidInput  | Pass         |
| testInvalidInputC3       | (5,4,8.8)         | InvalidInput     | InvalidInput  | Pass         |

While still not perfect, we only have a small thing to fix. And once that's done, we have all 21 of our test cases passing now. The [output for test run 4](./Output%20Files/TestRun4.txt) is shown below:
| **Test ID**              | **Input**         | **Expected Results** | **Actual Result** | **Pass or Fail** |
| :----------------------- | :---------------: | :---------------- | :------------- | :------------: |
| testRightTriangleA       | (3,4,5)           | Right            | Right         | Pass         |
| testRightTriangleB       | (5,3,4)           | Right            | Right         | Pass         |
| testRightTriangleC       | (4,5,3)           | Right            | Right         | Pass         |
| testEquilateralTriangleA | (1,1,1)           | Equilateral      | Equilateral   | Pass         |
| testEquilateralTriangleB | (15,15,15)        | Equilateral      | Equilateral   | Pass         |
| testEquilateralTriangleC | (50,50,50)        | Equilateral      | Equilateral   | Pass         |
| testScaleneTriangleA     | (1,2,3)           | Scalene          | Scalene       | Pass         |
| testScaleneTriangleB     | (5,3,7)           | Scalene          | Scalene       | Pass         |
| testScaleneTriangleC     | (8,9,2)           | Scalene          | Scalene       | Pass         |
| testIsocelesTriangleA    | (3,3,5)           | Isoceles         | Isoceles      | Pass         |
| testIsocelesTriangleB    | (5,3,5)           | Isoceles         | Isoceles      | Pass         |
| testIsocelesTriangleC    | (8,2,2)           | Isoceles         | Isoceles      | Pass         |
| testInvalidInputA1       | (250,15,15)       | InvalidInput     | InvalidInput  | Pass         |
| testInvalidInputA2       | (15,215,15)       | InvalidInput     | InvalidInput  | Pass         |
| testInvalidInputA3       | (5,20,201)        | InvalidInput     | InvalidInput  | Pass         |
| testInvalidInputB1       | (15,20,-3)        | InvalidInput     | InvalidInput  | Pass         |
| testInvalidInputB2       | (15,-20,30)       | InvalidInput     | InvalidInput  | Pass         |
| testInvalidInputB3       | (0,20,19)         | InvalidInput     | InvalidInput  | Pass         |
| testInvalidInputC1       | (True,20,19)      | InvalidInput     | InvalidInput  | Pass         |
| testInvalidInputC2       | (80,False,19)     | InvalidInput     | InvalidInput  | Pass         |
| testInvalidInputC3       | (5,4,8.8)         | InvalidInput     | InvalidInput  | Pass         |

Once we run code coverage again we can see that the report is now displaying 100% code coverage after those fixes and updated test cases:
```
Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
TestTriangle.py      52      0   100%
Triangle.py          14      0   100%
-----------------------------------------------
TOTAL                66      0   100%
```

### Part 4: Test Report
Now that we have 100% code coverage and all our test cases passing, we can report the results of the 4 test runs and what they led to.
|                | **Test Run 1** (Part 1) | **Test Run 2** (Part 2) | **Test Run 3** | **Test Run 4** |
| :------------- | :-----------------: | :-----------------: | :--------: | :--------: |
| Tests Planned  | 12                  | 12                  | 21         | 21         |
| Tests Executed | 12                  | 12                  | 21         | 21         |
| Tests Passed   | 0                   | 12                  | 20         | 21         |
| Defects Found  | 1                   | 5                   | 1          | 0          |
| Defects Fixed  | 1                   | 5                   | 1          | 0          |

Test run 1 and 2 used the same test set as one another and were developed with the focus on simply correctly classifying the triangles. Once that one line of code that all the test cases in test run 1 was fixed, test run 2 revealed the logical errors in the code when it came to correctly classifying triangles. 

Test run 3 and 4 used the first set of test cases but added additional ones on to account for the InvalidInput scenarios in the beginning of the `classifyTriangle()` function. While running test run 3 only caught one error, it was still an important catch in the overall code. And then test run 4 was ran to ensure that all errors were accounted for and that all test cases passed.

The strategy for deciding on a sufficient number of test cases came from the idea that I wanted to ensure the code was able to correctly classify each type of triangle in a way where each layout of a triangle was given as the input to the `classifyTriangle()` function. This resulted in the 3 test cases per type of triangle which led to the original 12 test cases. The decision to add on test cases to account for InvalidInputs came from running code coverage to see that roughly 20% of the `Triangle.py` code had been missed by the original test cases. Like the strategy for designing the triangle test cases, I wanted to come up with enough tests to test for each input value a, b, and c as an invalid input and make sure the code caught it. Once I developed those additional 9 test cases and added them to the original 12, we got a total of 21 test cases, but when I ran code coverage, the report indicated 100% coverage and I was satisfied with the number of test cases I had.
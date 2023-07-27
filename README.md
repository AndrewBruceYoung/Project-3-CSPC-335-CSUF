Project 3

Summer 2023 CPSC 335 - Algorithm Engineering

Deadline: 07/24 on Canvas

Instructor: Prof. Sampson Akwafuo

Abstract
In this project, you will develop greedy and/or exhaustive search/optimization, and approximation
algorithms for solving graph’s minimum spanning tree and the Fibonacci problems. The time
complexity of your algorithms will be either exponential, linear or polynomial.

Problem 1: Minimum Cost Graph Transversal
Assume that you are given an adjacency list representation of a weighted, undirected graph with
at least one node. The number of vertices in the graph is equal to the length of edges , where each
index i in edges contains vertex i 's siblings, in no particular order. Each of these siblings is an
array of length two, with the first value denoting the index in the list that this vertex is connected
to, and the second value denoting the weight of the edge. Note that this graph is undirected,
meaning that if a vertex appears in the edge list of another vertex, then the inverse will also be true
(along with the same weight).

This description corresponds to a well-known algorithm.
Develop and write an algorithm to return new edges array that represents a minimum spanning
tree. As discussed, the minimum spanning tree is a tree containing all of the vertices of the original
graph and a subset of the edges. These edges should connect all of the vertices with the minimum
total edge weight and without generating any cycles. If the graph is not connected, your algorithm
should return the minimum spanning forest (i.e. all of the nodes should be able to reach the same
nodes as they could in the initial edge list). Note that the graph represented by edges will not
contain any self-loops (vertices that have an outbound edge to themselves) and will only have
positively weighted edges (i.e., no negative distances).

Sample Input:
edges = [

[[1, 3], [2, 5]],

[[0, 3], [2, 10], [3, 12]],

[[0, 5], [1, 10]],

[[1, 12]]

]

Sample Output
[

[[1, 3], [2, 5]],

[[0, 3], [3, 12]],

[[0,5]],

[[1,2]]

]

Problem 2: The Fibonacci Problem and the Golden Ratio
In Fibonacci sequence, each member (or the Fibonacci number, 𝐹(n)) is obtained by calculating the
sum of two preceding members. Example of a sequence of Fibonacci numbers is shown below:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

Mathematically, the Fibonacci sequence contains series of 𝐹n such that

𝐹(n) = 𝐹(n-1) + 𝐹(n-2) if 𝑛 > 2

𝐹(n) = 1 if n = 1

𝐹(n) = 0 if n = 0

There are some efficient algorithms for solving this problem. Some of these approaches will reduce
the running time complexity while increasing the space requirement. The dynamic programming
approach is one of them and will be discussed in subsequent weeks.

For this project, you are expected to develop two algorithms to solve the Fibonacci problem.

A. The Exhaustive Pattern
The first approach will involve recursive calculation of each member of the sequence.

a. Using the formular above, develop a recursive algorithm to calculate the 𝑛𝑡ℎ terms of the
sequence. The first term of the sequence is 0, as shown above.

b. Print out the 15 th term of the sequence.

B. The Golden Ratio Approach
The ratio of any two successive members of a Fibonacci sequence i.e. (𝑓(n+1)/𝐹(n)) is known as the
golden ratio, phi. This ratio approximates 1.61803.

A Fibonacci number (a member of the sequence) can be calculated using the formula:

𝐹(n) = (((1+√5)^n)-((1-√5)^n)/(2^n)(√5))

In relations to a previous member of the sequence, the 𝑛𝑡ℎ term of the sequence can be calculated
using:

𝐹(n) ≈ (𝐹(p))((1+√5)/2)^(n-p)

Where 𝐹(p) represents any of the preceding terms of 𝐹(n) . Recall that (1+√5)/2 is equal to 1.61803 and
thus maybe substituted.

An approximation of the next term of the sequence can also be obtained by multiplying the
preceding term by the Golden Ratio

𝐹(n+1) ≈ (𝐹(p))((1+√5)/2)

There is a maxim that the ratio of two consecutive Fibonacci numbers approaches the Golden
Ratio, as 𝑛 gets bigger.

a. Design algorithms to obtain the Fibonacci numbers using equations (4) and (5) above
When implementing equation (4), ask the user to enter 'p'. You should specify that ‘p’
should be a positive integer and non-floating point. If a wrong number is entered, inform
the user and request for a new number, until a correct input is received. Use equation (3)
to obtain 𝑓(p). Then ask the user to enter ‘n’. Use the calculated 𝑓(p) to obtain 𝑓(n).

When implementing equation (5), equation (3) should be used to find 𝑓(n)

b. Print the first 20 terms of the sequence, from equations (4) and (5)

c. Compare your outputs when equation (4) is used against results from equation (5)

d. Check and confirm or disprove the maxim above using 𝐹(3)/𝐹(2) and 𝐹(30)/𝐹(29) (from equation
5 implementation)

To Do

1. Produce a written project report in PDF format. Your report should include:
a. Your name(s), CSUF-supplied email address(es), and an indication that the
submission is for project 3.

2. Develop the pseudocodes for Problem/Part 1, Part 2A and Part 2B. Implement the three
algorithms in either Python or C++

3. Your codes should be saved and submitted in the corresponding executable files (.py or
.cpp). Your codes should include your name and should be well-commented, and if done
in group, your code should contain names of every group member.

4. Mathematically analyze each algorithm and state the big O efficiency class. You may use
any of the methods discussed in class, including step counts.

5. Test your problem 1’s algorithm using the given sample input file. Include your result in
the PDF report.

Grading Rubric
The suggested grading rubric is given below:

Part 1 (30)
a. Clear and complete Pseudocode = 5 points
b. Mathematical analysis and correct Big O efficiency class = 5 points
c. Successful compilation of codes and presence of comments/names = 13 points
d. Accurate results (using the given sample input) = 7 points

Part 2A (35)
a. Clear and complete Pseudocode = 10 points
b. Mathematical analysis and correct Big O efficiency class = 5 points
c. Successful compilation of codes and presence of comments/names = 15 points
d. Produces accurate result (15th term) = 5 points

Part 2B (35)
a. Clear and complete Pseudocode, using equation 4 and 5 = 10 points
b. Mathematical analysis and correct Big O efficiency class = 5 points
c. Successful compilation of codes and presence of comments/names= 15 points
d. Checking if the user input, p, is a non-floating point positive integer = 5 points
e. Printing the first 20 terms of the sequence = 5 points
f. Comparison of outputs from both equations = 5 points
g. Confirming or disproving the maxim = 5 points
Ensure your submissions are your own works. Be advised that your submissions may be checked
for plagiarism using automated tools.
Submitting Your Code
Submit your files to the Project 3 Assignment on Canvas. It allows for multiple submissions. You
can submit your files separately only (do not zip or use .rar)
Deadline
The project deadline is Monday, July 24, by 11:59 pm on Canvas.
Penalty for late submission (within 48 hours) is as stated in the syllabus. Projects submitted more
than 48 hours after the deadline will not be accepted

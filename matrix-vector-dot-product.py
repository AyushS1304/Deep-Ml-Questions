# Matrix-Vector Dot Product
# Problem Statement

# Write a Python function that computes the dot product of a matrix and a vector. The function should return a list representing the resulting vector if the operation is valid, or -1 if the matrix and vector dimensions are incompatible. A matrix (a list of lists) can be dotted with a vector (a list) only if the number of columns in the matrix equals the length of the vector. For example, an n x m matrix requires a vector of length m.

# You may assume the input matrix is a valid (non-jagged) list of lists and the vector is a non-empty list.

# Example:
# Input:
# a = [[1, 2], [2, 4]], b = [1, 2]
# Output:
# [5, 10]
# Reasoning:
# Row 1: (1 * 1) + (2 * 2) = 1 + 4 = 5; Row 2: (2 * 1) + (4 * 2) = 2 + 8 = 10

# solution

#using " zip" to iterate through both lists simultaneously and calculate the dot product for each row of the matrix with the vector. The function checks for dimension compatibility before performing the calculations.
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	#base case
	if len(a[0])!= len(b):
		return -1
	
	result=[]
	for i in a:
		result.append(sum(x*y for x,y in zip(i,b)))
	
	return result


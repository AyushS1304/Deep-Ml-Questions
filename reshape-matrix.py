# Reshape Matrix
# Easy
# Linear Algebra


# Write a Python function that reshapes a given matrix into a specified shape. if it cant be reshaped return back an empty list []

# Example:
# Input:
# a = [[1,2,3,4],[5,6,7,8]], new_shape = (4, 2)
# Output:
# [[1, 2], [3, 4], [5, 6], [7, 8]]
# Reasoning:
# The given matrix is reshaped from 2x4 to 4x2.

# Solution 
import numpy as np

def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    arr = np.array(a)

    # Check if reshape is possible
    if arr.size != new_shape[0] * new_shape[1]:
        return []
    reshaped_matrix = arr.reshape(new_shape).tolist()
    return reshaped_matrix
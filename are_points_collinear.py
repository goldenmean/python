
"""
Given a set of points, where each element is an integer array containing an x and y value, return whether or not all the points exist on the same line.

Ex: Given the following points…

points = [[1, 2], [3, 2]], return true.
Ex: Given the following points...

points = [[1, 2], [3, 2], [-1, -1]], return false.
"""

from typing import List

def are_points_collinear(points: List[List[int]]) -> bool:
    if len(points) <= 2:
        return True  # Two or fewer points are always collinear

    # Function to calculate slope between two points
    def slope(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:  # Vertical line
            return float('inf')
        return (y2 - y1) / (x2 - x1)

    # Get the slope between the first two points
    initial_slope = slope(points[0], points[1])

    # Check if all other points have the same slope with the first point
    for i in range(2, len(points)):
        if slope(points[0], points[i]) != initial_slope:
            return False

    return True

# Test cases
print(are_points_collinear([[1, 2], [3, 2]]))  # True
print(are_points_collinear([[1, 2], [3, 2], [-1, -1]]))  # False
print(are_points_collinear([[1, 1], [2, 2], [3, 3]]))  # True
print(are_points_collinear([[1, 1], [2, 2], [3, 4]]))  # False
print(are_points_collinear([[0, 0], [0, 1], [0, 2]]))  # True (vertical line)
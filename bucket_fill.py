'''
You are Given an image represented as a matrix. Each value in the matrix represents the color of an individual pixel. Given a new color represented as an integer and a starting row and column, transform every adjacent pixel to the starting pixel that has the same color to the new color.
Note: This is effectively implementing a “bucket fill” in a software like Microsoft paint.

Ex: Given the following image, row, column, and color…

image = [
  [0,1,1],
  [0,1,0],
  [1,1,1]
], row = 1, column = 1, color = 3 modify image to be as follows...
image = [
  [0, 3, 3],
  [0, 3, 0],
  [3, 3, 3],
]

'''

# BFS algorithm is used to implement bucket fill 
#It uses a Queue to store the x,y coordinates of the pixels to be filled.

from collections import deque

def bucket_fill(image, row, column, color):
    
    pixels_to_fill = deque([(row, column)])
    original_color = image[row][column]

    while pixels_to_fill:
        row, column = pixels_to_fill.popleft()
        image[row][column] = color

        for (x, y) in [(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)]:
            if 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == original_color:
                pixels_to_fill.append((x, y))

    return image


image = [
  [0,1,1],
  [0,1,0],
  [1,1,1]
]
row = 1; col = 1; color = 3
#row = 1; col = 2; color = 3

print(bucket_fill(image, row, col, color))



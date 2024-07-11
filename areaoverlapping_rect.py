
'''
Given two rectangles on a 2D graph, return the area of their intersection. 
If the rectangles don't intersect, return 0.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
and

{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}
return 6.
'''

def calculate_intersection_area(rect1, rect2):
    # Unpack the top left corners and dimensions of both rectangles
    x1, y1 = rect1["top_left"]
    w1, h1 = rect1["dimensions"]
    x2, y2 = rect2["top_left"]
    w2, h2 = rect2["dimensions"]
    
    # Calculate the bottom right corner of both rectangles
    x1_br = x1 + w1
    y1_br = y1 - h1
    x2_br = x2 + w2
    y2_br = y2 - h2
    
    print(f"Rect1:TL = {x1,y1} ; BR = {x1_br,y1_br} ")
    print(f"Rect2:TL = {x2,y2} ; BR = {x2_br,y2_br} ")
    # Determine the overlap by comparing the x and y coordinates
    #overlapping width is minimum x coordinate of the bottom right corner points among 2 rectangles 
    # minus maximum x coordinate of the top left corner points among 2 rectangles
    overlap_width = min(x1_br, x2_br) - max(x1, x2)

    #overlapping height is minimum y coordinate of the bottom right corner points among 2 rectangles 
    # minus maximum y coordinate of the top left corner points among 2 rectangles    
    overlap_height = min(y1, y2) - max(y1_br, y2_br)
    print(overlap_width, overlap_height)
    
    # If there is no overlap, return 0
    if overlap_width <= 0 or overlap_height <= 0:
        return 0
    
    # Otherwise, calculate the area of the intersection
    intersection_area = overlap_width * overlap_height
    return intersection_area

# Define the rectangles
rect1 = {
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
rect2 = {
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}

# Calculate the intersection area
intersection_area = calculate_intersection_area(rect1, rect2)
print(intersection_area)
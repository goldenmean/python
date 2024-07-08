'''
You are given two rectangles as integer arrays and want to determine if they overlap.
Each rectangle will be given as two point, [x1, y1, x2, y2] where (x1, y1) represents
the bottom-left hand corner a rectangle and (x2, y2) represents the top-right hand 
corner of a rectangle. Given two arrays that represent rectangles, rect1 and rect2, 
return whether or not they overlap.
Note: Two rectangles overlap if the area of their intersection is positive.

Ex: Given the two rectangles, rect1 and rect2...

rect1 = [0, 0, 1, 1], rect2 = [0, 0, 3, 3], return true.
Ex: Given the two rectangles, rect1 and rect2...

rect1 = [0, 0, 1, 1], rect2 = [1, 1, 4, 4], return false.
'''

def are_rect_overlapping(rect1, rect2) -> bool:
    if rect2[2] > rect1[0] and rect2[3] > rect1[1] and rect2[0] < rect1[2] and rect2[1] < rect1[3]:
        return True
    else:
        return False
    
    #return max(rect1[0], rect2[0]) < min(rect1[2], rect2[2]) and max(rect1[1], rect2[1]) < min(rect1[3], rect2[3])

#rect1 = [0, 0, 1, 1] ; rect2 = [0, 0, 3, 3]
rect1 = [0, 0, 1, 1]; rect2 = [1, 1, 4, 4]

print(are_rect_overlapping(rect1, rect2))   


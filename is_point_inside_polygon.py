#Given a polygon and a point, find if this point is inside the polygon

def is_point_inside_polygon(polygon, p):
    n = len(polygon)
    inside = False
    
    for i in range(n):
        j = (i + 1) % n
        xi, yi = polygon[i]
        xj, yj = polygon[j]
        
        #l1 = ((yi > p[1]) != (yj > p[1])) 
        #l2 = (p[0] < (xj - xi) * (p[1] - yi) / (yj - yi) + xi)
        #intersect = l1 and l2 
        #print(f"{l1} {l2} {intersect}")
        intersect = ((yi > p[1]) != (yj > p[1])) and (p[0] < (xj - xi) * (p[1] - yi) / (yj - yi) + xi)
        print(f"intersect is {intersect}")
        if intersect:
            inside = not inside
    
    return inside

# Example usage
polygon = [(0, 0), (2, 0), (2, 2), (0, 2)]
point = (1, 1)

result = is_point_inside_polygon(polygon, point)
print(f"Is the point {point} inside the polygon? {result}")

# Test with a point on the boundary
boundary_point = (1, 0)
#result = is_point_inside_polygon(polygon, boundary_point)
#print(f"Is the point {boundary_point} inside the polygon? {result}")

# Test with a point outside the polygon
outside_point = (3, 3)
#result = is_point_inside_polygon(polygon, outside_point)
#print(f"Is the point {outside_point} inside the polygon? {result}")
#Calculate given row k of a pascal's triangle
"""
In Pascal's triangle, each number can be calculated using combinations,
specifically nCr where n is the row number (k in our code) and r is the
position in that row (i in our code).
The formula comes from the relationship between consecutive elements in 
the same row. Let's break it down:
For row k, any element at position i is: C(k,i) = k! / (i! * (k-i)!)
To get the next element, we need: C(k,i+1) = k! / ((i+1)! * (k-(i+1))!)
The relationship between these consecutive elements is: 
C(k,i+1) = C(k,i) * (k-i)/(i+1)
"""

def pascals_triangle(k):
    # Initialize the row with first element as 1
    row = [1]
    
    # Calculate each element using the previous element
    for i in range(k):
        # Multiply by (k-i) and divide by (i+1)
        next_val = row[i] * (k - i) // (i + 1)
        row.append(next_val)
    
    return row

# Example usage
k = 4
result = pascals_triangle(k)
print(result)  # Output: [1, 4, 6, 4, 1]

# Test with other rows
print(pascals_triangle(0))  # Output: [1]
print(pascals_triangle(1))  # Output: [1, 1]
print(pascals_triangle(2))  # Output: [1, 2, 1]
print(pascals_triangle(3)) 
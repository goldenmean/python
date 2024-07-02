


def calculate_depth(nested_list,depth):
    # Base case: if the list is empty, return 0
    if not nested_list:
        return 0
    
    res = 0    
    for item in nested_list:
        # Check if the current item is a list
        if isinstance(item, list):
            # Recursively calculate the depth for this sublist
            res += calculate_depth(item,depth+1)
        else:
            # If the item is an integer, add its depth to the total count
            res += item*depth
    
    return res

# Example usage
nested_list = [[1, 1], 2, [1, 1]]
depth=1
result = calculate_depth(nested_list, depth)
print(result) 

# Stack based iterative implementation
def calculate_depth_iterative(nested_list):
    # Stack to keep track of sublists and their depths
    stack = [(nested_list, 1)]
    
    res = 0
    while stack:
        # Pop the top item from the stack
        sublist, depth = stack.pop()
        
        for item in sublist:
            # If the item is a list, push it onto the stack with increased depth
            if isinstance(item, list):
                stack.append((item, depth + 1))
            else:
                # If the item is an integer, add its depth-adjusted value to the total count
                res += item * depth
    
    return res

nested_list = [[1, 1], 2, [1, 1]]
#nested_list = [1, 1, 2, [1, 1]]
#nested_list=[]
result = calculate_depth_iterative(nested_list)
print(result) 

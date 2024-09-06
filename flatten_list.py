'''
Flatten a nested list (any depth)
'''

def flatten_list(nested_list):
    flat_list = []
    
    def _flatten(sublist):
        for item in sublist:
            if isinstance(item, list):
                _flatten(item)
            else:
                flat_list.append(item)
    
    _flatten(nested_list)
    return flat_list

# Example usage:
nested_list = [1, [2, [3, 4], 5], [6, 7], [8, [9, [10]]]]
#nested_list = [[1], 2, [[3,4], 5], [[[]]], [[[6]]], 7, 8, []]
flattened = flatten_list(nested_list)
print(flattened)
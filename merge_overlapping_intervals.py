'''
merge any overlapping intervals 

'''


def merge_intervals(intervals): 

    # Sort the intervals by their start time 

    sorted_intervals = sorted(intervals, key=lambda x: x[0]) 

    # Initialize the merged list with the first interval 
    merged = [sorted_intervals[0]] 

    for current in sorted_intervals: 
        # Get the last element in the merged list 
        last = merged[-1]
        print(f"current is {current}")
        print(f"last is {last}")

        # If the current interval overlaps with the last one, merge them 
        if current[0] <= last[1]: 
            last[1] = max(last[1], current[1]) #when we change last[1] it changes the corresponding value of merged[-1]
            print(f"last: modified to {last}")
        else: 
            # Add the current interval to the merged list 
            merged.append(current) 
            print(f"merged is {merged}")

    return merged 
 

# Test the function 

intervals = [[1, 3], [5, 12], [4, 10], [20, 25]] 

#intervals = [(1, 3), (5, 12), (4, 10), (20, 25)] #If we use tuples, it gives TypeError as tuple' object does not support item assignment

print(merge_intervals(intervals)) 
'''
In academia, the h-index is a metric used to calculate the impact of a researcher's papers. 
It is calculated as follows:

A researcher has index h if at least h of her N papers have h citations each. If there are
multiple h satisfying this formula, the maximum is chosen.

For example, suppose N = 5, and the respective citations of each paper are [4, 3, 0, 1, 5].
Then the h-index would be 3, since the researcher has 3 papers with at least 3 citations.

Given a list of paper citations of a researcher, calculate their h-index.
'''

def calculate_h_index(citations):
    # Sort the citations in descending order
    citations.sort(reverse=True)
    
    h_index = 0
    for i, citation in enumerate(citations):
        # if citiation of 1st index is greater than 1(i+1 i=0 for 1st value), then h_index =(i+1) which is 1
        # then continue checking if current citation is greater than the current index i+1  , that means we can increase 
        # the h_index to 2 ( i is 1 for 2nd value so i+1 = 2)
        if citation >= i + 1:
            h_index = i + 1
        else:
            #We break because in a sorted array any citation after this will be less than it, so stop search here
            break
            
    return h_index

# Example usage
#citations = [4, 3, 0, 1, 5]
citations = [8, 2, 10, 9, 5]
#citations = [8, 0, 0 , 0, -1]
#citations = [9, 8, 7, 9, 3, 7, 6]
h_index = calculate_h_index(citations)
print(f"The h-index is: {h_index}")  


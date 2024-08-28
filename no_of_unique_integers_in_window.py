'''
Given a list of integers, find the number of unique integers in each window of size k 
Example: 
 list: [1, 2, 2, 4, 5] 
 k = 3 
 answer: [2, 2, 3] 
'''

def unique_integers_in_windows(nums, k):
    if not nums or k <= 0:
        return []

    from collections import defaultdict

    freq = defaultdict(int)
    unique_counts = []
    unique_in_current_window = 0

    for i in range(len(nums)):
        # Add the current number to the frequency dictionary
        if freq[nums[i]] == 0:
            unique_in_current_window += 1
        freq[nums[i]] += 1

        # Remove the element that is sliding out of the window
        if i >= k:
            if freq[nums[i - k]] == 1:
                unique_in_current_window -= 1
            freq[nums[i - k]] -= 1

        # Record the count of unique integers for the current window
        if i >= k - 1:
            unique_counts.append(unique_in_current_window)

    return unique_counts

# Example usage
nums = [1, 2, 2, 4, 5]
k = 3
print(unique_integers_in_windows(nums, k))  # Output: [2, 2, 3]
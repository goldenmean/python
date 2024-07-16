'''
Given an integer array, nums, return a list containing all subsets of nums that contain
 at least two elements and have an increasing sequence.

Ex: Given the following nums…

nums = [1, 2, 3], return [[1,2],[1,2,3],[1,3],[2,3]].
Ex: Given the following nums…

nums = [2, 4, 3, 5], return [[2,4],[2,4,5],[2,3],[2,3,5],[2,5],[4,5],[3,5]].
'''


def find_subsequences(nums):
    def backtrack(start, path):
        print(f"backtrack start={start}, path={path}")
        if len(path) >= 2:
            print(f"Appending path to res: {path}")
            res.append(path)
        for i in range(start, len(nums)):
            print(f"i={i}, path={path}")
            # Ensure increasing order
            if not path or nums[i] > path[-1]:
                backtrack(i + 1, path + [nums[i]])
        print(f"returning from backtrack start={start}, path={path}")

    res = []
    backtrack(0, [])
    return res

# Example usage
nums1 = [1, 2, 3]
#print(find_subsequences(nums1))
nums2 = [2, 4, 3, 5]
print(find_subsequences(nums2))
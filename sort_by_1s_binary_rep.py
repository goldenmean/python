

def sort_by_1s_in_binary_rep(nums):
    return sorted(nums, key=lambda x: (bin(x).count('1'), x))


nums = [5, 2, 8]
#nums = [4, 5, 5, 1, 3, 9]
res=sort_by_1s_in_binary_rep(nums)
print(res)
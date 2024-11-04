"""
Given a list whose elements indicate maximum jumps from that index to right, 
return the minimum number of jumps needed to reach the end of the list.
"""


def min_number_of_jumps(nums):
    if nums[0] == 0:
        return -1

    if len(nums) == 1:
        return 0
    
    #DP array indicating minimum number of jumps needed to reach index i
    min_jumps = [float("+inf")]*len(nums)
    min_jumps[0] = 0
    #Another array to store source index from which we can jump to index i in least number of jumps
    jmp_src_idx = [-1]*len(nums)

    # Dynamic programming solution
    # fill the DP Array min_jumps[ ] where value at index i in this array 
    # indicates minimum number of jumps needed to reach index i from any previous 
    # index j such that 0 <= j < i
    for i in range(1,len(nums)):
        for j in range(i):
            # check if we can jump to index i from index j
            if nums[j] + j >= i:
                # check if existing value of min_jumps[j] + 1 is less than the current value of min_jumps[i]
                # only then update the value of min_jumps[i]
                if min_jumps[j] + 1 < min_jumps[i]:
                   min_jumps[i] = min_jumps[j] + 1
                   #update the source index array
                   jmp_src_idx[i] = j
    

    print("min_jumps array:", min_jumps)
    print(f"source index array: {jmp_src_idx}")
    
    prev = jmp_src_idx[-1]
    tmp=[len(nums)-1]
    while prev != -1:
        tmp.append(prev)
        prev = jmp_src_idx[prev]

    print(f"Path of indices with minimum cost jump is:")
    tmp=tmp[::-1]
    print("->".join([str(x) for x in tmp]))

    return -1 if min_jumps[-1] == float("+inf") else min_jumps[-1] 


#num=[2,3,1,1,4] # 1st function from top fails this case 
#num=[2,0,1,0,4]
num=[2,3,0,0,2,1,4]
#num=[2,2,0,0,2,1,4]
#num=[2,1,0,0,2,1,4]
print(min_number_of_jumps(num))
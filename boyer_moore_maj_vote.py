def boyer_moore_maj_vote(nums):
    count = 0
    candidate = None
    for num in nums: 
        if count == 0: 
            candidate = num 

        if candidate == num: 
            count+=1 
        else: 
            count-=1 

    return candidate 
	


arr=[2,2,1,1,2,6]

print(boyer_moore_maj_vote(arr))
'''
A ship is about to set sail and you are responsible for its safety precautions. 
More specifically, you are responsible for determining how many life rafts to carry onboard. 
You are given a list of all the passengers’ weights and are informed that a single life raft has
 a maximum capacity of limit and can hold at most two people. Return the minimum number of life 
 rafts you must take onboard to ensure the safety of all your passengers. Note: You may assume that
 a the maximum weight of any individual is at most limit.

Ex: Given the following passenger weights and limit…

weights = [1, 3, 5, 2] and limit = 5, return 3
weights = [1, 2] and limit = 3, return 1
weights = [4, 2, 3, 3] and limit = 5 return 3
'''

def no_of_life_rafts(nums,limit):
    rafts=0
    sum=0
    cnt=0
    
    nums.sort()
    for n in nums:
        sum+=n
        cnt+=1
        if sum >= limit or cnt == 2:
            rafts+=1
            if sum > limit:
                sum=n
            else:
                sum=0
    #print(f"in the end, sum is {sum}")
    if sum!=0 and sum <= limit:        
        rafts+=1

    return rafts

#weights = [1, 3, 5, 2]
#limit=5
#weights = [1, 2]
#limit=3
#weights = [4, 2, 3, 3]
#limit=5
weights = [1,2,1]
limit=5

print(no_of_life_rafts(weights,limit))
rcnt = 0
'''	
def permutations(nums):
    perms=[]
    soln=[]

	
    def backtrack():
        global rcnt	
        rcnt += 1
        print("Soln", soln)		                				

        print("Entering backtrack count is",rcnt)        		
        if len(nums) == len(soln):
            perms.append(soln[:])
            print("permutation",soln)
            print("A: Returning from backtrack count is",rcnt) 			
            rcnt -= 1			
            print("A: Returning to backtrack count ",rcnt)
            return 

        for n in nums:
            #print("A",nums)	            		
            print("Number",n)
            if not n in soln:
                soln.append(n)
                backtrack()
                soln.pop()
                print("Soln after popping",soln)
        print("B: Returning from backtrack count is",rcnt) 							
        rcnt -= 1
        print("B: Returning to backtrack count ",rcnt)		
		
    backtrack()
    return perms


nums=[1,2,3]
print(permutations(nums))
'''	
	
	
def get_permutations(numbers):
    # If the list is empty, there are no permutations
    if len(numbers) == 0:
        return []

    # If there is only one element in the list, only one permutation is possible
    if len(numbers) == 1:
        return [numbers]

    # Generate permutations for lists with more than one element
    permutations = [] # resulting list
    for i in range(len(numbers)):
       m = numbers[i]
       remaining_list = numbers[:i] + numbers[i+1:]
       for p in get_permutations(remaining_list):
           permutations.append([m] + p)
    return permutations

numbers = [1, 2, 3]
permutations = get_permutations(numbers)

for p in permutations:
    print(p)


'''
def get_permutations(numbers):
    # Start with the empty list
    permutations = [[]]
    
    for n in numbers:
        new_permutations = []
        
        for perm in permutations:
            # Insert the number at every possible position
            for i in range(len(perm)+1):
                new_permutations.append(perm[:i] + [n] + perm[i:])
                
        permutations = new_permutations
    
    return permutations

numbers = [1, 2, 3]
permutations = get_permutations(numbers)

for p in permutations:
    print(p)
'''

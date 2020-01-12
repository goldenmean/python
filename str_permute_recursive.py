def permutations(word): 
    if len(word)<=1: 
        return [word]   
        #get all permutations of length N-1 
    perms=permutations(word[1:]) 
    char=word[0] 
    result=[] 
    #iterate over all permutations of length N-1 
    for perm in perms: 
        #insert the character into every possible location 
        for i in range(len(perm)+1): 
            result.append(perm[:i] + char + perm[i:]) 
    return result
        
"""		
def  permutations_iter(word):
    while True:
        perms = []
        result = []
        
        char = word[0]
        new_word = word[1:]
        
        if len(new_word)==2: 
            perms = [new_word,''.join(reversed(new_word))]
        
        for perm in perms: 
            #insert the character into every possible location 
            for i in range(len(perm)+1): 
                result.append(perm[:i] + char + perm[i:]) 
        return result
        
        if len(new_word)==2:
            break;
        
"""
def perms(word):
    stack = list(word)
    results = [stack.pop()]
    while len(stack) != 0:
        c = stack.pop()
        new_results = []
        for w in results:
            for i in range(len(w)+1):
                new_results.append(w[:i] + c + w[i:])
        results = new_results
    return results
	
#print permutations("LSE")       
#print permutations_iter("SE")       
print perms("LSE") 


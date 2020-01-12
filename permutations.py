#Generate permutations of a given numbers
import itertools
a=[1,2,3,4,5]
#print "Ajit",'-->',a[0],'-->','Deshpande'

#print([x for x in itertools.permutations('12345')])
print "####################"
#print([x for x in itertools.permutations(a)])
print "####################"
permuted_a = [x for x in itertools.permutations(a)]
len_perm = len(permuted_a)
print permuted_a

"""for i in range(len_perm):
    print permuted_a[i][0],'-->',permuted_a[i][1],'-->',permuted_a[i][2],'-->',permuted_a[i][3],'-->',permuted_a[i][4]
"""
    
    
	
	



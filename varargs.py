#!/usr/bin/python
def varargs(*var_tuple): #no required argument , can be called with no arguments as well
    for var in var_tuple:
	    print(var)
    print("arguments provided", len(var_tuple))	

		
varargs(10)
varargs(42,"Ajit",16)
varargs()


'''
# Function definition is here # one positional argument always needed in printinfo call
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print("Output is: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )
printinfo( 'a' )
'''
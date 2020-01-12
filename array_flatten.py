def flatten(mylist):
	i=0
	while i<len(mylist):
		while True:
			try:
				mylist[i:i+1] = mylist[i]
			except (TypeError, IndexError):
				break
		i += 1
 
mylist = [[1], 2, [[3,4], 5], [[[]]], [[[6]]], 7, 8, []]
print mylist
flatten(mylist)
print mylist
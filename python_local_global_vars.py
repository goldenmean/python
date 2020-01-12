i=333


def test():
    print "Global i =", i
    
    for i in range(10):
        print "Local i = ",i
        
test()      
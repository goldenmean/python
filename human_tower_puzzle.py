#!/usr/bin/python
#This function takes a list of tuples. Tuple(n):(height,weight) of nth person
def htower_len(ht_wt):
    ht_sorted = sorted(ht_wt,reverse=True)
    wt_sorted = sorted(ht_wt,key=lambda ht_wt:ht_wt[1])
    max_len = 1 
    
    
    #print "Sorted by height" ; print ht_sorted
    #print "Sorted by weight" ; print wt_sorted
    
    len1 = len(ht_sorted)
    i=0
    j=0
    while i < (len1-1):
        if(ht_sorted[i+1][1] < ht_sorted[0][1]):
            max_len = max_len+1
        i=i+1           
    
    print "maximum tower length :" ,max_len

testcase =1	
print "Result of Test case ",testcase   
htower_len([(5,75),(6.7,83),(4,78),(5.2,90)])

testcase = testcase + 1
print "Result of Test case ",testcase   
htower_len([(65, 100),(70, 150),(56, 90),(75, 190),(60, 95),(68, 110)])

testcase = testcase + 1
print "Result of Test case ",testcase   
htower_len([(3,2),(5,9),(6,7),(7,8)])	
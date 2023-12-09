"""
Isolated conundrum #129

A list of 5 positive integers has mean 5, mode 5, median 5, range 5 and duplicate numbers are allowed. How many such lists of 5 positive integers are there?
"""
startlist = [0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,6,6,6,6,6,7,7,7,7,7,8,8,8,8,8,9,9,9,9,9,10,10,10,10,10]


#import itertools
#from scipy import stats
import random

def findmean(lst):
    mean = sum(lst)/len(lst)
    return (mean)

def findmedian(lst):
    srted = sorted(lst)
    return int(srted[2])

def findmode(lst):
    #return int(stats.mode(lst))
    return max(set(lst), key=lst.count)

def findrange(lst):
    return int(lst[4] - lst[0])

cnt = 0
#print(startlist)
while True:
    thislist = sorted(random.sample(startlist, 5))
    #print(thislist)
    mean = findmean(thislist)
    mode = findmode(thislist)
    median = findmedian(thislist)
    range = findrange(thislist)
    #print(mean, mode, median, range)
    if(mean == 5 and mode == 5 and median == 5 and range == 5):
        cnt = cnt + 1
        print(thislist, mean, mode, median, {cnt})
    continue




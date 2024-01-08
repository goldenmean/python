'''
In a given array of numbers, one element will show up once and the others will each show up twice.
 Can you find the number that only appears once in O(n) linear time? 
 Bonus points if you can do it in O(1) space as well.
'''


def lonely_number(arr):
    d={}
    
    for num in arr:
        if num in d:
            d[num]+=1            
        else:
            d[num]=1
            
    for k,v in d.items():
        if v==1:
            return k

    return -1
    
#arr=[1,4,7,9,4,1,7]
#arr=[1]
#arr=[1,2,3,4]
#arr=[1,1,2,3,4,6,6,4,2,3]
#arr=[]
arr=[-1,1]

print(lonely_number(arr))

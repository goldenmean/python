'''
Given two integer arrays, nums1 and nums2, return the intersection of the two arrays
 (i.e. the elements they have in common).

Ex: Given the following nums1 and nums2...

nums1 = [1, 2, 2, 3], nums2 = [0, 2, 2, 5], return [2, 2].
'''

from collections import Counter

def intersection(nums1, nums2):
    d1={}
    d2={}
    d1=Counter(nums1)
    d2=Counter(nums2)
    res=[]
    for i in d1:
        if i in d2:
            cnt=min(d1[i],d2[i])
            res+=[i]*cnt
    
    return res

#print(intersection([1, 2, 2, 3, 2], [0, 2, 2, 2, 5]))
print(intersection([1, 2, 3, 4], [0, 1.1, 2.2, 3.5, 4.001]))




'''
You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].

For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).

Return an array answer where answer[i] is the answer to the ith query.

'''
from functools import reduce 

def xorQueries(arr, queries):
    res = []
    dres = dict()
    for l,r in queries:
        if (l,r) not in dres:
            tmplst = arr[l:r+1]
            curres = reduce(lambda x,y:x^y,tmplst)
            dres[(l,r)]=curres
            res.append(curres)
        else:
            res.append(dres[(l,r)])                              
        
    return res


##
def efficientxorQueries(arr, queries):
       
        n = len(arr)
        prefix = [0] * n
        ans = []

        # Fill the prefix XOR array
        prefix[0] = arr[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] ^ arr[i]

        # Process each query
        for left, right in queries:
            if left == 0:
                ans.append(prefix[right])
            else:
                ans.append(prefix[right] ^ prefix[left - 1])

        return ans

            
'''
Given an integer array, nums that represents the score of a spelling bee’s
 contestants, return string array that represents each of their respective placings.

Ex: Given the following nums…

nums = [3, 1, 4, 2, 5], return ["Bronze Medal","5","Silver Medal","4","Gold Medal"]
'''

def placings(nums):
    dres={} #dictionary of the scores {score:index of the score}
    for i in range(len(nums)):
        dres[nums[i]]=i

    print(dres)

    sdres = dict(sorted(dres.items(),key=lambda item: item[0],reverse=True)) #sorted by key values, i.e. scores
    pos = 1
    output=[0]*len(nums)
    for k,v in sdres.items():
        if pos == 1:
            output[v]="Gold Medal"            
        elif pos == 2:
            output[v]="Silver Medal"
        elif pos == 3:
            output[v]="Bronze Medal"
        else:
            output[v]=pos

        pos += 1

    return output

nums = [3, 1, 4, 2, 5]

print(placings(nums))




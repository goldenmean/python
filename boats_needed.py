

def boats_needed(weights,limit):
    weights.sort()
    boats = 0
    left = 0
    right = len(weights) - 1
    while left <= right:
        # this checks if weight at index left & right can fit in the boat
        #if they fit, they get one boat and 
        # then we move both left +=1 and right -= 1 to compare next two weights
        if weights[left] + weights[right] <= limit:
            #if they are overweight , the right weight needs a boat for itself
            # since we are within weight, we move to left pointer to next weight
            left += 1
        # we decrement right index by 1 either case of whether w[l] + w[r] <= limit or over limit
        # so that we can compare next two weights
        right -= 1
        # we increment boat
        boats += 1
    return boats



import math 

def cumulative_likes(n):
    cum_likes = 0
    shared = 5
    liked = 0

    for i in range(1,n+1):
        liked = math.floor(shared/2)
        cum_likes += liked
        shared = liked*3

    return cum_likes


n=1
print(cumulative_likes(n))

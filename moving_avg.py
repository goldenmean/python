'''
This question is asked by Microsoft. Design a class, MovingAverage, which contains a method,
next that is responsible for returning the moving average from a stream of integers.
Note: a moving average is the average of a subset of data at a given point in time.

Ex: Given the following series of events...

// i.e. the moving average has a capacity of 3.
MovingAverage movingAverage = new MovingAverage(3);
m.next(3) returns 3 because (3 / 1) = 3
m.next(5) returns 4 because (3 + 5) / 2 = 4 
m.next(7) = returns 5 because (3 + 5 + 7) / 3 = 5
m.next(6) = returns 6 because (5 + 7 + 6) / 3 = 6
'''

prev_2 = 0
prev_1 = 0
cnt = 0

def mov_avg(num):    
    global prev_2, prev_1
    global cnt
    cnt+=1
    d = 3 if cnt >= 3 else cnt
    mavg = (prev_2 + prev_1 + num)/d
    prev_2 = prev_1
    prev_1 = num
    
    return mavg
    
print(mov_avg(3))
print(mov_avg(5))
print(mov_avg(7))
print(mov_avg(6))
print(mov_avg(0))
print(mov_avg(10))

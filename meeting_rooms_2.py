'''
Leetcode: Meeting Rooms 2
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.
Example1
Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)

Example2
Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room

'''

def meeting_rooms_2(intervals ):
    intervals.sort(key = lambda x: x[0]) 
    if len(intervals) == 0:
        return 0
    cr = 1 # number of conference rooms 

    for i in range(1,len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            cr+=1

    return cr


#intervals = [(0,30),(5,10),(15,20)]
intervals = [(2,7)]

cr=meeting_rooms_2(intervals)
print(f"Number of conference rooms needed: {cr}")

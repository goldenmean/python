'''
Consider you are given a shop and the arriving and leaving times of all the customers in a day.
How could you calculate the maximum number of customers who were in the shop at the same time
'''

def max_customers(arrivals, departures):
    events = [(time, 1) for time in arrivals] + [(time, -1) for time in departures]
    events.sort()  # Sort all events by time
    print(events)

    max_count = 0
    current_count = 0

    for _, change in events:
        current_count += change
        max_count = max(max_count, current_count)

    return max_count


print(max_customers([1, 9, 2, 4], [8, 11, 6, 10])) 




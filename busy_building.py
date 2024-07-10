'''
You are given a list of dictionaries habing data entries that represent entries and exits of people
into a building. An entry looks like this:

{"timestamp": 1526579928, count: 3, "type": "enter"}

This means 3 people entered the building. An exit looks like this:

{"timestamp": 1526580382, count: 2, "type": "exit"}

This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people in the building.
Return it as a pair of (start, end) timestamps. You can assume the building always starts off 
and ends up empty, i.e. with 0 people inside.
'''

def find_busiest_period(data):
    # Step 1: Sort the data by timestamp
    data.sort(key=lambda x: x['timestamp'])
    
    max_people = 0
    current_people = 0
    busiest_start = None
    busiest_end = None
    previous_timestamp = None
    
    for i, entry in enumerate(data):
        if entry['type'] == 'enter':
            current_people += entry['count']
        else:  # 'exit'
            current_people -= entry['count']
        
        # Check if this is the last entry or if the next timestamp is different
        if i + 1 == len(data) or data[i + 1]['timestamp'] != entry['timestamp']:
            if current_people > max_people:
                max_people = current_people
                busiest_start = previous_timestamp if previous_timestamp else entry['timestamp']
                busiest_end = entry['timestamp']
            previous_timestamp = entry['timestamp']
    
    return (busiest_start, busiest_end)

# Example usage
data = [
    {"timestamp": 1526579928, "count": 3, "type": "enter"},
    {"timestamp": 1526580382, "count": 2, "type": "exit"},
    {"timestamp": 1526580482, "count": 5, "type": "enter"},
    {"timestamp": 1526580582, "count": 3, "type": "exit"}
]

print(find_busiest_period(data))
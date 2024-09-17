



from collections import defaultdict

a = [3, 2, 1, 2, 3]

# Create a defaultdict with list as the default factory
d = defaultdict(list)

# Populate the defaultdict so keys are the list elements, values are the indices of those elements
for index, value in enumerate(a):
    d[value].append(index)

print(d)


#Just a way to create a regular dictionary with key, values, values as list of size of a
regular_d={n:[0]*len(a) for n in a}

# Another way without using defaultdict , but instead using a regular dictionary
regular_d = {}
for index, value in enumerate(a):
    if value not in regular_d:
        regular_d[value] = []
    regular_d[value].append(index)

print(regular_d)

'''
CSV file parsing, manipulating
'''

import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# Reading csv file in a dictionary format
data = {}
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    #reader has list of dictionaries - one for each row 
    for row in reader:
        #row is one row = {'id': '123', 'name': 'John Doe'}
        #Store the row in the dictionary: data, where its key is value of the id column: "123" and 
        # value of data is the full row
        data[row['id']] = row

# Accessing data
print(data['123']['name'])



# Writing csv file
data = [
    {'id': '1', 'name': 'John Doe'},
    {'id': '2', 'name': 'Jane Smith'}
]

with open('output.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=['id', 'name'])
    writer.writeheader()
    writer.writerows(data)


# Read CSV file
data = []
with open('input.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        data.append(row)

# Process data
processed_data = [[int(row[0]), float(row[1])] for row in data]

# Write processed data to CSV file
with open('output.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'value'])  # Header
    writer.writerows(processed_data)



#CSV reading and writing using Pandas
import pandas as pd

# Read CSV file
df = pd.read_csv('data.csv')

# Perform operations
df['total'] = df['column1'] + df['column2']

# Write changes back to CSV
df.to_csv('updated_data.csv')